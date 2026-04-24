import React from 'react';
import { TrendingDown, TrendingUp } from 'lucide-react';

const RankingHeader = () => {
    // 내 순위, 총 참가자 수, 총 자산, 수익률 표시할거임
    const my_rank = 16;
    const total_count = 20;
    const total_assets = 50000000;
    const profit_rate = 0.0;
    //////////////////////////////////////////////////

    return (<>
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-sm text-white/80">내 순위</p>
                    <p className="mt-1 text-4xl font-light">{my_rank}위</p>
                </div>

                <div className="text-right">
                    <p className="text-sm text-white/80">총 참가자</p>
                    <p className="mt-1 text-2xl font-semibold">{total_count}명</p>
                </div>
            </div>

            <div className="my-6 h-px bg-white/20" />

            <div className="grid grid-cols-2 gap-6">
                <div>
                <p className="text-sm text-white/80">총 자산</p>
                <p className="mt-1 text-xl font-semibold">₩{total_assets.toLocaleString()}</p>
                </div>

                <div>
                    <p className="text-sm text-white/80">수익률</p>
                    <div className="mt-1 flex items-center gap-1">
                        {profit_rate >= 0 ? (
                        <TrendingUp size={18} className="text-white" />
                        ) :
                        <TrendingDown size={18} className="text-white" />
                        }

                        <span className="text-xl font-semibold">
                            {profit_rate >= 0 ? " +" : " "}
                            {profit_rate.toFixed(2)}%
                        </span>
                    </div>
                </div>
            </div>
        </>
    );
};

export default RankingHeader;