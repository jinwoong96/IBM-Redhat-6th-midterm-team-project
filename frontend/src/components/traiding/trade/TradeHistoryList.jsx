import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTrade } from './../../../Slice/tradeSlice';

const TradeHistoryList = () => {
    const dispatch = useDispatch();
    const tradeList = useSelector((state) => state.trade.trades);

    useEffect(() => {
        dispatch(fetchTrade());
    }, [dispatch]);

    return (
        <div style={{ padding: '20px' }}>
            <h3>최근 거래 내역</h3>
            <ul style={{ listStyle: 'none', padding: 0 }}>
                {tradeList.map((trade, index) => (
                    <li 
                        key={trade.trade_id || index} 
                        style={{
                            display: 'flex',
                            flexDirection: 'column',
                            padding: '15px',
                            borderBottom: '1px solid #eee',
                            marginBottom: '10px',
                            borderRadius: '8px',
                            backgroundColor: '#fff',
                            boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
                        }}
                    >
                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                            <span style={{ fontWeight: 'bold', fontSize: '1.1rem' }}>
                                {trade.item_code}
                            </span>
                            <span style={{ 
                                color: trade.buy_type === '매수' || trade.buy_type === 'BUY' ? '#e74c3c' : '#3498db',
                                fontWeight: 'bold'
                            }}>
                                {trade.buy_type}
                            </span>
                        </div>

                        <div style={{ display: 'flex', justifyContent: 'space-between', color: '#555', fontSize: '0.9rem' }}>
                            <div>
                                <span>가격: <strong>{trade.price?.toLocaleString()}원</strong></span>
                                <span style={{ margin: '0 10px' }}>|</span>
                                <span>수량: <strong>{trade.quantity}주</strong></span>
                            </div>
                            <div style={{ color: '#999' }}>
                                {new Date(trade.trade_day).toLocaleDateString()}
                            </div>
                        </div>

                        <div style={{ marginTop: '5px', fontSize: '0.8rem', color: '#bbb' }}>
                            사용자: {trade.login_id}
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TradeHistoryList;