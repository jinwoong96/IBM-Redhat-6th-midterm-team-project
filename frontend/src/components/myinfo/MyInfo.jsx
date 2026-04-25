import { Calendar, Mail, TrendingDown, TrendingUp, User } from 'lucide-react';
import React from 'react';
import { CONSTANTS_CONFIG } from '@/config';

const MyInfo = () => {
    //////////// 닉네임, 아이디, 생성일, 현금+평가금액 불러옴
    const nickname = "투자왕";
    const login_id = "testuser01";
    const date_created = "생성 날짜";
    const cash = 35000000;
    const stock = 10000000;
    /////////////////////////////////////////////////////
    const seed_money = CONSTANTS_CONFIG.SEED_MONEY;
    const total_assets = cash + stock;
    const profit = total_assets - seed_money;
    const profit_rate = profit / seed_money * 100;

    const edit_my_info = () => {
        alert("내 정보 수정 클릭 시 실행");
    }

    return (<>
            <div className="flex items-center gap-6">
                <div className="flex h-20 w-20 items-center justify-center rounded-full bg-linear-to-br from-blue-500 to-purple-600 text-white">
                    <User size={42} />
                </div>

                <div>
                    <div className="flex items-center gap-3">
                        <h2 className="text-2xl font-semibold text-gray-800">{nickname}</h2>
                        <button
                            onClick={()=>edit_my_info()} 
                            className="text-xs font-medium text-blue-500 hover:underline hover:cursor-pointer">
                            내 정보 수정
                        </button>
                    </div>

                    <div className="mt-3 flex items-center gap-5 text-sm text-gray-500">
                        <span className="flex items-center gap-1">
                            <User size={16} />
                            {login_id}
                        </span>
                        <span className="flex items-center gap-1">
                            <Calendar size={16} />
                            {date_created}
                        </span>
                    </div>
                </div>
            </div>

            <div className="my-7 border-t border-gray-100" />

            <div className="grid grid-cols-3 gap-8">
                <div>
                    <p className="text-sm text-gray-500">총 자산</p>
                    <p className="mt-2 text-2xl font-semibold text-gray-900">₩{total_assets.toLocaleString()}</p>
                </div>
                <div>
                    <p className="text-sm text-gray-500">수익금</p>
                    <p className="mt-2 text-2xl font-semibold text-emerald-500">
                        {profit>=0?"+":""}₩{profit.toLocaleString()}</p>
                </div>
                <div>
                    <p className="text-sm text-gray-500">수익률</p>
                    <div className="mt-2 flex items-center text-2xl font-semibold text-emerald-500">
                        {profit_rate>=0?<TrendingUp size={18} />:<TrendingDown size={18} />}
                        <span className="ml-1">
                            {profit_rate>=0?" +":" "}
                            {profit_rate.toFixed(2)}%
                        </span>
                    </div>
                </div>
            </div>
        </>
    );
};

export default MyInfo;