// import React from 'react';
import FilterButtonArea from './FilterButtonArea';
import StockList from './StockList';

///////////////////////////////////////
import React, { useEffect, useState } from 'react'; 
import { useSelector, useDispatch } from 'react-redux';
import { fetchChart_code, fetchChartUser, toggleWish, syncWishlist } from '../../../Slice/chartuserSlice'; 
import { addWishlistAsync, delWishlistAsync,fetchWishlistAsync } from '../../../Slice/wishlistSlice';
/////////////////////////////////////

const StockListArea = () => {

    //////////////////////////////////////////////////
    const dispatch = useDispatch();
    
    const stockData = useSelector((state) => state.chartuser.chartuserlist);
    const items = stockData?.list || [];
    const handleWishClick = (e, stock) => {
    e.stopPropagation(); 
    dispatch(toggleWish(stock.item_code));

    if (!stock.is_wish) { //아직 dispatch전이라 업뎃안됨
        dispatch(addWishlistAsync(stock.item_code));
    } else {
        dispatch(delWishlistAsync(stock.item_code));
    }
    };
    useEffect(() => { // useEffect는 async 가 불가해서 await 쓰기위해
                        // 함수 넣음
        const init = async () => {
            if (items.length === 0) {
                await dispatch(fetchChartUser());
            }
            const result = await dispatch(fetchWishlistAsync());
            const wishCodes = (result.payload || []).map(w => w.item_code);
            dispatch(syncWishlist(wishCodes));
        };
        init();
    }, [dispatch]);
    //////////////////////////////////////////////////////

    const [isWish, setIsWish] = useState(false);

    return (
        <>
            <div className="border-b border-gray-100 px-4 py-3">

            {/* //////////////////////////////////////////////////////////////////////// */}
                <h2>{stockData?.item_name || "종목 리스트"}</h2> 

                {items.length > 0 ? (
                    items.map((stock) => (
                        <div 
                            key={stock.item_code} 
                            onClick={() => dispatch(fetchChart_code(stock.item_code))} 
                            style={{ 
                                borderBottom: '1px solid #ccc', 
                                padding: '10px',
                                cursor: 'pointer', 
                                transition: 'background-color 0.2s'
                            }}
                            onMouseOver={(e) => e.currentTarget.style.backgroundColor = '#f9f9f9'}
                            onMouseOut={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
                        >
                            <h4>{stock.item_name} ({stock.item_code})</h4>
                            
                            <p>카테고리: {stock.category_name}</p>
                            <p>현재가: {stock.end_price?.toLocaleString()}원</p>
                            <p>수익률: {stock.flu_range_percent}%</p>
                            <p onClick={(e) => handleWishClick(e, stock)} style={{ cursor: 'pointer' }}>
                                찜 여부: {stock.is_wish ? "❤️" : "🤍"}
                            </p>
                        </div>
                    ))
                ) : (
                    <p>데이터를 불러오는 중입니다...</p>
                )}
                {/* ///////////////////////////////////////////////////////////// */}

                <div>
                    <div className="inline-block border-b-2 border-blue-500 pb-2 text-sm font-semibold text-blue-600">
                        국내주식
                    </div>
                </div>
                <FilterButtonArea />
            </div>
            <StockList />
        </>
    );
};

export default StockListArea;