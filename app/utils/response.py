import uuid
from typing import Any, Optional
from fastapi.responses import JSONResponse

from app.core.context import get_trace_id

class ApiResponse:
    @staticmethod
    def success(
        data: Any = None, 
        message: str = "Operation successful", 
        status_code: int = 200
    ) -> JSONResponse:
        """
        Standard Success Response
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "success": True,
                "message": message,
                "data": data,
               "trace_id": get_trace_id()
            }
        )

    @staticmethod
    def error(
        message: str = "An error occurred", 
        data: Any = None, 
        status_code: int = 400
    ) -> JSONResponse:
        """
        Standard Error Response
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "message": message,
                "data": data,
                "trace_id": get_trace_id()
            }
        )