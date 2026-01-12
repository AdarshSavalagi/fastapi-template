import logging
import sys
from pythonjsonlogger import jsonlogger
import colorlog
from app.core.context import get_trace_id
from app.core.config import settings

# 1. Custom Filter to inject Trace ID into Log Records
class TraceIdFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = get_trace_id()
        return True

def setup_logging():
    """
    Configures the root logger to output to Console.
    Format depends on settings.LOG_FORMAT (json vs console).
    """
    # 1. Get Root Logger
    logger = logging.getLogger()
    logger.setLevel(settings.LOG_LEVEL)
    
    # Remove default handlers (uvicorn/fastapi often add their own)
    if logger.hasHandlers():
        logger.handlers.clear()

    # 2. Create Handler (Stream to Console/Docker Stdout)
    handler = logging.StreamHandler(sys.stdout)
    
    # 3. Add Filter (Inject Trace ID)
    trace_filter = TraceIdFilter()
    handler.addFilter(trace_filter)

    # 4. Set Formatter based on Config
    if settings.LOG_FORMAT == "json":
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(trace_id)s %(message)s %(name)s",
            datefmt="%Y-%m-%dT%H:%M:%S"
        )
    else:
        # Development: Colored Console Format
        formatter = colorlog.ColoredFormatter(
            "%(asctime)s | %(log_color)s%(levelname)-8s%(reset)s | %(cyan)s[%(trace_id)s]%(reset)s | %(name)s | %(message)s",
            datefmt="%H:%M:%S",
            reset=True,
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white',
            },
            secondary_log_colors={
                'message': {
                    'ERROR': 'red',
                    'CRITICAL': 'red'
                }
            }
        )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 5. Tweak Uvicorn/FastAPI Loggers to use our setup
    # This ensures internal server logs also get formatted
    logging.getLogger("uvicorn.access").handlers = [handler]
    logging.getLogger("uvicorn.error").handlers = [handler]
    logging.getLogger("uvicorn").handlers = [handler]