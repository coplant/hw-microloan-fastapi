import sys
from pathlib import Path
from urllib.request import Request

import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

sys.path.append(str(Path(__file__).parents[1] / 'alembic_fake'))
sys.path.append("..")

from auth.router import router as router_auth
from auth.router import users as router_users
from loan.router import router as router_loan
from verification.router import router as router_verification
from operation.router import router as router_operator
from manager.router import router as router_manager
from accountant.router import router as router_accountant

app = FastAPI(title="ЧВК")
router = APIRouter(prefix="/api")


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


router.include_router(router_auth)
router.include_router(router_users)
router.include_router(router_loan)
router.include_router(router_verification)
router.include_router(router_operator)
router.include_router(router_manager)
router.include_router(router_accountant)
app.include_router(router)

origins = [
    "http://localhost:3000",
    "https://coplant.duckdns.org",
    "localhost"
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
