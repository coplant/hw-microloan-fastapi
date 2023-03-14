from fastapi import FastAPI

from auth.router import router as router_auth

app = FastAPI(title="ЧВК")

app.include_router(router_auth)
