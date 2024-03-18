from fastapi import FastAPI
from financial.routes import financial_routes

app = FastAPI()

app.include_router(financial_routes.router)