from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, async_engine
from fastapi.concurrency import asynccontextmanager
from dotenv import load_dotenv
import os
from app.routers import balance, chart_user, news_user, progress, ranking, trade, user, wishlist


load_dotenv(dotenv_path=".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
   
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await async_engine.dispose()

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     
    allow_credentials=True,     
    allow_methods=["*"],       
    allow_headers=["*"],       
)

app.include_router(balance.router)
app.include_router(chart_user.router)
app.include_router(news_user.router)
app.include_router(progress.router)
app.include_router(ranking.router)
app.include_router(trade.router)
app.include_router(user.router)
app.include_router(wishlist.router)

