import React from 'react';
import { CONSTANTS_CONFIG } from "@/config";

const AccountSummary = () => {
    //////////// 내 잔고 총 자산(현금+평가금액), 현재 수익률 데이터 가져오기(위에서 props로 받는지 여기서 리덕스로 받는지는 모르겠음)
    const seed_money = CONSTANTS_CONFIG.SEED_MONEY
    const total_assets = 50000000; // 저장소에서 가져온거
    const profit = total_assets - seed_money;
    const profit_rate = profit / seed_money * 100;
    /////////////////////////////////////////////////////////////////

    return (
        <div className="overflow-hidden rounded-2xl bg-linear-to-br from-blue-500 via-indigo-500 to-purple-600 p-4 text-white shadow-md">
            <div className="text-sm opacity-80">총 자산</div>
            <div className="mt-2 text-4xl font-bold">₩{total_assets.toLocaleString()}</div>
            <div className="mt-4 text-sm opacity-80">{`~ ₩${profit.toLocaleString()} (${profit_rate>=0?"+":""}${profit_rate.toFixed(2)}%)`}</div>
        </div>
    );
};

export default AccountSummary;