from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, async_engine
from fastapi.concurrency import asynccontextmanager
from dotenv import load_dotenv
from app.routers import balance, chart_user, news_user, progress, ranking, trade, user, wishlist
from app.core.auth import get_current_user # 실제 로그인 함수 임포트

load_dotenv(dotenv_path=".env")

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await async_engine.dispose()

app = FastAPI(lifespan=lifespan)


app.include_router(balance.router)
app.include_router(chart_user.router)
app.include_router(news_user.router)
app.include_router(progress.router)
app.include_router(ranking.router)
app.include_router(trade.router)
app.include_router(user.router)
app.include_router(wishlist.router)

# 1. 가짜 유저 객체 만들기 (우리가 DB에 넣은 user01 역할을 할 녀석)
class MockUser:
    login_id = "user01"

# 2. 가짜 로그인 함수 만들기
async def mock_get_current_user():
    return MockUser()

# 3. 실제 로그인 함수를 가짜 함수로 통째로 갈아끼우기 (핵심!)
app.dependency_overrides[get_current_user] = mock_get_current_user