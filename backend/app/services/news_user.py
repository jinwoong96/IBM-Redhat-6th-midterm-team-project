from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.crud.news import NewsCrud
from app.db.crud.news_user import NewsuserCrud
from app.db.crud.effects import EffectsCrud
from app.db.models.news import News
import random
from app.db.crud.chart_user import ChartuserCrud
from app.db.scheme.chart_user import ChartuserUpdate
class NewsuserService:

    @staticmethod #사용자의 과거뉴스기록 조회
    async def my_newsuser(login_id:str,limit:int, db:AsyncSession): #해당유저의 전체기록조회
        history=await NewsuserCrud.get_by_login_id(login_id,limit,db)

        if not history: #예외 : 기록이 없을때 (1일차)
            return []
        
        history.sort(key=lambda x:x.day, reverse=True)
        
        history_list=[]

        for i in history:
            news_data={
                'day':i.day,
                'news_id':i.news_id,
                'news_title':i.news.news_title,
                'news_comments':i.news.news_comments
            }
            history_list.append(news_data)
        
        return history_list if limit!=1 else history_list[0]


    @staticmethod
    async def add_newsuser(login_id:str,db:AsyncSession): #새로운 날짜의 뉴스를 랜덤배정 후 기록
        all_news=await NewsCrud.get_all_news(db) 
        seen_news=await NewsuserCrud.get_by_login_id(login_id,30,db) #사용자가 지금까지 본 뉴스 아이디 리스트
        seen_ids = {s.news_id for s in seen_news} #가져온 뉴스리스트에서 다시for문 돌려서 뉴스 아이디만 뽑아서
        last_day = max([s.day for s in seen_news], default=0)
        next_day = last_day + 1
        unseen_news = [n for n in all_news if n.news_id not in seen_ids] #안본 뉴스 중 하나를 고른다
        
        if not unseen_news:
            raise HTTPException(status_code=404,detail='새로운 뉴스가 없습니다')#만약 뉴스가 더없다면..
        
        select_random_news=random.choice(unseen_news)#랜덤으로 뉴스를 뽑는다
        res_news_id = select_random_news.news_id
        res_news_title = select_random_news.news_title
        res_news_comments = select_random_news.news_comments

        await NewsuserCrud.create(#새로 배정된 뉴스를 db에저장 근데 이거 다음날 뉴스라서 저장할때 +1이 맞지않나?(해결)
            login_id=login_id,
            news_id=select_random_news.news_id,
            day=next_day,
            db=db
        )

        effects= await EffectsCrud.get_by_news_id(select_random_news.news_id, db) #랜덤으로 배정된 뉴스 아이디에 따른 영향카테고리 가져옴

        category_effect=[] #뉴스당 카테고리가 여러개이므로 가져와서 담을 빈 배열만들어주고
        for i in effects:#영향 카테고리 에서 반복문돌려서 카테고리마다 지정된 등락폭안에서 랜덤 설정
            effect_flu=random.randint(int(i.flu_min),int(i.flu_max))

            category_effect.append({ #빈 배열 안에 넣어줌
                'category_name':i.category_name,
                'flu_value':effect_flu
            })

        user_current_stock=await ChartuserCrud.get_item_list_crud(login_id,db) #가장최신날짜의 종목들을 다 가져와서
        for stock in user_current_stock:# 그 안에있는 종목들을 가져와서
            apply_flu=None
            for i in category_effect:#카테고리별 영향을 반복해서 돌린후
                if i['category_name'] == stock['category_name']:#지정된 뉴스에 나온 종목이름과 전체종목이름중 같은게 있으면
                    apply_flu=i['flu_value']#지정된 등락폭으로 확정
                    break

            if apply_flu is None:#영향없는 종목들은 -3~3퍼센트의 등락률 지정
                apply_flu = round(random.uniform(-3.0, 3.0), 2)

            next_start_price=stock['end_price']#다음날 시작가 
            next_flu_range=round(next_start_price*(apply_flu/100))#다음날 전날대비 등락률
            next_end_price=next_start_price+next_flu_range#다음날 종가

            next_max_price = max(next_start_price,next_end_price)*(1+random.uniform(0,0.01))#종가나 시가 중 높은금액에 살짝 더높은 최고가
            next_min_price = min(next_start_price,next_end_price)*(1-random.uniform(0,0.01))#종가나 시가 중 낮은금액에 살짝 더낮은 최저가

            next_max_price = round(next_max_price)
            next_min_price = round(next_min_price)

            await ChartuserCrud.create_all(
                user_id=login_id,
                chart=ChartuserUpdate(
                        item_code=stock['item_code'],
                        start_price=next_start_price,
                        end_price=next_end_price,
                        max_price=next_max_price,
                        min_price=next_min_price,
                        day=next_day,
                        flu_range=next_flu_range,
                        flu_range_percent=apply_flu
                    ),
                    db=db
                )
        await db.commit()

        return{"news_id": res_news_id,
                "news_title": res_news_title,
                "news_comments": res_news_comments
                }