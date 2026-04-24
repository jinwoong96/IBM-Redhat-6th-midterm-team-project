import React from 'react';

const BalanceSummary = () => {
    /////////////// 보유 현금, 보유 주식 평가액 합계 불러옴
    const money = 50000000;
    const val = 0;
    ///////////////////////////////////////////

    return (
        <div className="rounded-2xl border border-gray-200 bg-white p-4">
            <div className="mb-4 text-lg font-semibold">보유 현금</div>

            <div className="space-y-3 text-sm">
            <div className="flex items-center justify-between text-gray-500">
                <span>KRW</span>
                <span className="font-semibold text-gray-800">{`₩${money.toLocaleString()}`}</span>
            </div>

            <div className="flex items-center justify-between text-gray-500">
                <span>주식 평가액</span>
                <span className="font-semibold text-gray-800">{`₩${val.toLocaleString()}`}</span>
            </div>
            </div>
        </div>
    );
};

export default BalanceSummary;