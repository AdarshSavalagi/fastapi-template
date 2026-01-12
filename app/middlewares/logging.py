import time
import uuid
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.context import trace_id_ctx
from app.core.config import settings

logger = logging.getLogger("api")

# Optional Import (so app doesn't crash if libraries aren't installed)
try:
    from opentelemetry import trace
    tracer = trace.get_tracer(__name__)
except ImportError:
    tracer = None

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. FAIL-SAFE: Generate UUID locally (Works even if Tempo is down)
        # Check if client sent a trace-id (e.g. from Frontend), else generate new
        request_trace_id = request.headers.get("X-Trace-ID", str(uuid.uuid4()))
        trace_id_ctx.set(request_trace_id)

        start_time = time.time()
        
        # 2. OPTIONAL: OpenTelemetry Logic (Only if enabled)
        span = None
        if settings.ENABLE_TELEMETRY and tracer:
            span = tracer.start_span(f"{request.method} {request.url.path}")
            span.set_attribute("http.trace_id", request_trace_id)

        # 3. Log Entry
        logger.info(f"[{request_trace_id}] REQUEST: {request.method} {request.url.path}")

        try:
            # 4. Process Request
            response = await call_next(request)
            
            process_time = (time.time() - start_time) * 1000
            
            logger.info(
                f"[{request_trace_id}] RESPONSE: {response.status_code} "
                f"| Time: {process_time:.2f}ms"
            )
            
            # 5. Attach ID to Header so Client/Frontend can see it
            response.headers["X-Trace-ID"] = request_trace_id
            
            return response
            
        except Exception as e:
            # Log the error with the Trace ID so you can find it
            logger.error(f"[{request_trace_id}] ERROR: {str(e)}")
            if span:
                span.record_exception(e)
            raise e
            
        finally:
            # Close the OTel span
            if span:
                span.end()