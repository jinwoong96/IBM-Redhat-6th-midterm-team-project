import React, { useState } from 'react';
import StockItem from './StockItem';
import WishItem from './WishItem';
const StockList = () => {
    const [isWish, setIsWish] = useState(false);

    return (
        <div>
            <div>국내주식</div>
            <div>메뉴 선택</div>
            <button onClick={() => setIsWish(!isWish)}>
                {isWish ? '전체 종목 보기' : '관심종목 목록보기'}
            </button>
            
            {isWish ? <WishItem /> : <StockItem />}
        </div>
    );
};

export default StockList;