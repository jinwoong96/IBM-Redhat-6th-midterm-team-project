import React, { useState } from 'react';
import { useSelector,useDispatch } from 'react-redux';
import { addTradeAsync } from './../../../Slice/tradeSlice';
import { fetchMyBalance } from '../../../Slice/balanceSlice';
import { fetchUser } from '../../../Slice/userSlice';

const TradePanel = () => {
    const chartDataObj = useSelector((state) => state.chartuser.chartuserlist_code);
    const chartData = chartDataObj?.list || [];
    const dispatch = useDispatch();


    // 오름차순후 젤 마지막 값을 꺼내서 반환
    const latestData = [...chartData].sort((a, b) => a.day - b.day)[chartData.length - 1];


    const [quantity, setQuantity] = useState(0);

    const itemCode = latestData?.item_code || "종목 미선택";
    const unitPrice = latestData?.end_price || 0; 
    const totalPrice = unitPrice * quantity;

    const handleTrade = async(type) => {

        const tradeData = {
            item_code: itemCode,
            buy_type: type,
            price: unitPrice,
            quantity: quantity,
            trade_day: latestData.day >= 1 ? latestData.day : 1
            // 테스트를위해 일단 1넣음
        };

        await dispatch(addTradeAsync(tradeData));
        await dispatch(fetchMyBalance());
        await dispatch(fetchUser());
        setQuantity(0); // 입력창 초기화
    };
    return (
        <div>
            <h3>거래</h3>
            <hr />
            <div>종목: {itemCode}</div>
            <div>
                수량: 
                <input 
                    type="number" 
                    value={quantity} 
                    onChange={(e) => setQuantity(Number(e.target.value))} 
                />
            </div>
            <div>입력수량: {quantity}주</div>
            <div>1주 가격: {unitPrice.toLocaleString()}원</div>
            <div>총 금액: {totalPrice.toLocaleString()}원</div>
            
            <div style={{ marginTop: '10px' }}>
                <button onClick={() => handleTrade("buy")}>매수</button>
                <button onClick={() => handleTrade("sell")}>매도</button>
            </div>
        </div>
    );
};

export default TradePanel;