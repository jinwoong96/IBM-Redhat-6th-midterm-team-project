import React, { useEffect } from 'react'; 
import { useSelector, useDispatch } from 'react-redux';
import { fetchChart_code, fetchChartUser } from '../../../Slice/chartuserSlice'; 

const StockItem = () => {
    const dispatch = useDispatch();
    
    const stockData = useSelector((state) => state.chartuser.chartuserlist);
    const items = stockData?.list || [];

    useEffect(() => {
        dispatch(fetchChartUser());
    }, [dispatch]);

    return (
        <div>
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
                        <h4>{stock.item_code}</h4>
                        <p>카테고리: {stock.category_name}</p>
                        <p>현재가: {stock.end_price?.toLocaleString()}원</p>
                        <p>수익률: {stock.flu_range_percent}%</p>
                        <p>찜 여부: {stock.is_wish ? "❤️" : "🤍"}</p>
                    </div>
                ))
            ) : (
                <p>데이터를 불러오는 중입니다...</p>
            )}
        </div>
    );
};

export default StockItem;