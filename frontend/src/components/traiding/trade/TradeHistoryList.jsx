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
        <div>
            <h3>최근 거래 내역</h3>
            <hr />
            {tradeList.map((trade, index) => (
                <div key={trade.trade_id || index}>
                    <div>
                        {/* item_code가 안 뜨면 item_name이라도 뜨는지 확인 */}
                        <strong>[ {trade.item_name || trade.item_code || "이름없음"} ]</strong> 
                        <span> | 구분: {trade.buy_type === 'buy' ? '매수' : '매도'}</span>
                    </div>
                    <div>
                        <span>가격: {trade.price?.toLocaleString()}원 </span>
                        <span>수량: {trade.quantity}주</span>
                    </div>
                    <div>
                        <small>거래 시점: {trade.trade_day}일차 </small>
                        {/* login_id가 안 뜨면 '아이디 없음' 표시 */}
                        <small> | ID: {trade.login_id || "아이디 없음"}</small>
                    </div>
                    <hr />
                </div>
            ))}
        </div>
    );
};

export default TradeHistoryList;