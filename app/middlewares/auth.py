from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from app.constants.messages import ApiMessages
from app.constants.public_routes import PublicRoutes
from app.utils.jwt_helper import decode_token
from app.utils.response import ApiResponse


class JWTAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.public_paths = PublicRoutes.Routes

    async def dispatch(self, request: Request, call_next):
        # 1. Skip Auth for Public Paths
        if any(request.url.path.startswith(path) for path in self.public_paths):
            return await call_next(request)

        # 2. Extract Header
        auth_header = request.headers.get("Authorization")
        
        if not auth_header or not auth_header.startswith("Bearer "):
            return ApiResponse.error(
                message=ApiMessages.TOKEN_MISSING,  # <-- Use Constant
                status_code=401
            )

        token = auth_header.split(" ")[1]

        # 3. Decode & Validate Token
        payload = decode_token(token)
        
        if payload is None:
            return ApiResponse.error(
                message=ApiMessages.TOKEN_INVALID,  # <-- Use Constant
                status_code=401
            )

        # 4. Attach User to Request State
        request.state.user = payload

        response = await call_next(request)
        return response