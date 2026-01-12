from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from app.core.config import settings

def setup_telemetry(app):
    if not settings.ENABLE_TELEMETRY:
        return

    # 1. Set up the provider
    provider = TracerProvider()
    trace.set_tracer_provider(provider)

    # 2. Configure where to send data (Tempo/Jaeger)
    # If no endpoint is set, we can fallback to Console (prints to terminal) for debugging
    if settings.OTEL_EXPORTER_OTLP_ENDPOINT:
        exporter = OTLPSpanExporter(endpoint=settings.OTEL_EXPORTER_OTLP_ENDPOINT)
    else:
        exporter = ConsoleSpanExporter()

    provider.add_span_processor(BatchSpanProcessor(exporter))

    # 3. Auto-instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)

    # 4. Auto-instrument Database (SQLAlchemy)
    # You need to pass your 'engine' object here
    # from app.core.database import engine
    # SQLAlchemyInstrumentor().instrument(engine=engine)