import { ChevronDown } from 'lucide-react';
import React, { useState } from 'react';
import { useSelector,useDispatch } from 'react-redux';
import { addTradeAsync } from './../../../Slice/tradeSlice';
import { fetchMyBalance } from '../../../Slice/balanceSlice';
import { fetchUser } from '../../../Slice/userSlice';

// 오른쪽 매수/매도 패널
const TradePanel = () => {
    const chartDataObj = useSelector((state) => state.chartuser.chartuserlist_code);
    const chartData = chartDataObj?.list || [];
    const dispatch = useDispatch();


    // 오름차순후 젤 마지막 값을 꺼내서 반환
    const latestData = [...chartData].sort((a, b) => a.day - b.day)[chartData.length - 1];


    const [quantity, setQuantity] = useState(0);

    const itemCode = latestData?.item_code || "종목 미선택";
    const unitPrice = latestData?.end_price || 0; 
    // const totalPrice = unitPrice * quantity;

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
            <div className="rounded-2xl border border-gray-200 bg-white p-4">
                <div className="mb-4 text-lg font-semibold">거래</div>

                <label className="mb-2 block text-sm font-medium text-gray-600">
                수량
                </label>
                <div className="relative">
                <input
                    type="number"
                    value={quantity}
                    onChange={(e)=>{e.target.value>=0?setQuantity(e.target.value):0}}
                    className="w-full rounded-xl border border-blue-400 px-4 py-3 pr-10 outline-none focus:ring-2 focus:ring-blue-200"
                />
                </div>

                <div className="mt-4 space-y-2 text-sm text-gray-500">
                <div className="flex justify-between">
                    <span>수량</span>
                    <span>{quantity>0?quantity:"-"}</span>
                </div>
                <div className="flex justify-between">
                    <span>1주 가격</span>
                    <span>{unitPrice?unitPrice.toLocaleString():"-"}</span>
                </div>
                <div className="flex justify-between">
                    <span>총 금액</span>
                    <span>{quantity>0?(unitPrice*quantity).toLocaleString():"-"}</span>
                </div>
                </div>

                <div className="mt-5 grid grid-cols-2 gap-3">
                <button 
                    onClick={()=>handleTrade("buy")}
                    className="rounded-xl bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700">
                    매수
                </button>
                <button 
                    onClick={()=>handleTrade("sell")}
                    className="rounded-xl bg-rose-500 py-3 font-semibold text-white hover:bg-rose-600">
                    매도
                </button>
                </div>
            </div>
        </div>
    );
};

export default TradePanel;