import { ChevronDown } from 'lucide-react';
import React, { useState } from 'react';

// 오른쪽 매수/매도 패널
const TradePanel = () => {
    ///////////////// state 관리 현재 선택된 종목의 가격 가져옴
    ///////////////// 현금, 보유수량 정보도 추가로 있어야 매수, 매도 클릭했을 때 검증 들어갈 수 있음
    const price = 45000;
    /////////////////////////////////////////////////
    const [countInput, setCountInput] = useState(0);

    const onClickBuy = () => {
        alert("매수 클릭했을 때 실행");
    }

    const onClickSell = () => {
        alert("매도 클릭했을 때 실행");
    }

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
                    value={countInput}
                    onChange={(e)=>{e.target.value>=0?setCountInput(e.target.value):0}}
                    className="w-full rounded-xl border border-blue-400 px-4 py-3 pr-10 outline-none focus:ring-2 focus:ring-blue-200"
                />
                </div>

                <div className="mt-4 space-y-2 text-sm text-gray-500">
                <div className="flex justify-between">
                    <span>수량</span>
                    <span>{countInput>0?countInput:"-"}</span>
                </div>
                <div className="flex justify-between">
                    <span>1주 가격</span>
                    <span>{price?price.toLocaleString():"-"}</span>
                </div>
                <div className="flex justify-between">
                    <span>총 금액</span>
                    <span>{countInput>0?(price*countInput).toLocaleString():"-"}</span>
                </div>
                </div>

                <div className="mt-5 grid grid-cols-2 gap-3">
                <button 
                    onClick={onClickBuy}
                    className="rounded-xl bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700">
                    매수
                </button>
                <button 
                    onClick={onClickSell}
                    className="rounded-xl bg-rose-500 py-3 font-semibold text-white hover:bg-rose-600">
                    매도
                </button>
                </div>
            </div>
        </div>
    );
};

export default TradePanel;