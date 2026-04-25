import { Activity } from 'lucide-react';
import React from 'react';
import StatCard from '../common/StatCard';

const Statistics = () => {
    //////////// 매수 체결횟수, 매도 체결횟수, 현금, 평가금액 불러옴
    const count_buy = 2;
    const count_sell = 3;
    const cash = 30000000;
    const stock = 15000000;
    //////////////////////////////////////////////////////////

    const total_trade_count = count_buy + count_sell;

    return (
        <div>
            <h3 className="flex items-center gap-2 text-xl font-semibold text-gray-800">
                <Activity size={22} className="text-purple-500" />
                거래 통계
            </h3>

            <div className="mt-7 space-y-4">
                <div className="flex items-center justify-between rounded-xl bg-blue-50 px-4 py-4">
                    <span className="text-sm font-medium text-gray-600">총 거래 횟수</span>
                    <span className="text-xl font-semibold text-blue-500">{total_trade_count}회</span>
                </div>

                <div className="grid grid-cols-2 gap-4">
                    <StatCard label="매수" value={`${count_buy}회`} color="text-emerald-500" bg="bg-emerald-50" />
                    <StatCard label="매도" value={`${count_sell}회`} color="text-red-500" bg="bg-red-50" />
                    <StatCard label="현금보유량" value={`${cash.toLocaleString()}원`} color="text-purple-500" bg="bg-purple-50" />
                    <StatCard label="평가금액" value={`${stock.toLocaleString()}원`} color="text-orange-500" bg="bg-orange-50" />
                </div>
            </div>
        </div>
    );
};

export default Statistics;