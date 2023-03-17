from urllib.request import Request

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi_users import InvalidPasswordException
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from auth.router import router as router_auth
from auth.router import users as router_users
from loan.router import router as router_loan
from verification.router import router as router_verification
from operation.router import router as router_operator

app = FastAPI(title="ЧВК")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": "error",
            "data": None,
            "detail": exc.errors()
        },
    )


@app.exception_handler(HTTPException)
async def main_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "data": None,
            "detail": exc.detail
        },
    )


app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_loan)
app.include_router(router_verification)
app.include_router(router_operator)
# app.include_router(router_verification)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
