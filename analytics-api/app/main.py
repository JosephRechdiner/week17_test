from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes import analytics_router
from connection import SQLManager

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.sql_manager = SQLManager()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(analytics_router)