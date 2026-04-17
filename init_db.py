# import asyncio
# from database import async_engine, Base

# # 🚨 [매우 중요] 테이블로 만들 모든 모델을 반드시 여기에 import 해야 합니다!
# # import 하지 않으면 SQLAlchemy가 해당 모델의 존재를 몰라서 테이블을 만들지 않습니다.
# from models.user import User
# from models.item import Item
# from models.ranking import Ranking
# from models.chart_init import ChartInit
# from models.chart_user import ChartUser
# from models.trade import Trade
# from models.news import News
# from models.news_user import NewsUser
# from models.effects import Effects
# from models.balance import Balance
# from models.wish_list import WishList

# async def create_tables():
#     print("데이터베이스 연결 및 테이블 생성을 시작합니다...")
    
#     # async_engine을 사용하여 비동기적으로 테이블 생성
#     async with async_engine.begin() as conn:
#         # (선택) 기존 테이블을 모두 지우고 새로 만들고 싶다면 아래 주석을 해제하세요.
#         # await conn.run_sync(Base.metadata.drop_all)
        
#         # Base에 등록된 모든 모델을 기반으로 테이블 생성
#         await conn.run_sync(Base.metadata.create_all)
        
#     print("✅ 모든 테이블이 성공적으로 생성되었습니다!")

# if __name__ == "__main__":
#     asyncio.run(create_tables())