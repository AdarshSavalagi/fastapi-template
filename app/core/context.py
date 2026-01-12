import contextvars
import uuid

# Define a ContextVar (like ThreadLocal) to hold the Trace ID
# Default value is None
trace_id_ctx = contextvars.ContextVar("trace_id", default=None)

def get_trace_id() -> str:
    """Helper to get current trace_id or generate a new one if missing"""
    tid = trace_id_ctx.get()
    if not tid:
        return str(uuid.uuid4())
    return tid