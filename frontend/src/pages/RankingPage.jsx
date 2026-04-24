import React, { useState } from 'react';
import RankingHeader from '../components/ranking/RankingHeader';
import RankingTable from '../components/ranking/RankingTable';

const RankingPage = () => {


    const rankings = [
        { rank: 1, nickname: "투자의신", totalAsset: 64297147, profit: 14297147, rate: 28.59 },
        { rank: 2, nickname: "재테크고수", totalAsset: 63909077, profit: 13909077, rate: 27.82 },
        { rank: 3, nickname: "코스닥러버", totalAsset: 63834261, profit: 13834261, rate: 27.67 },
        { rank: 4, nickname: "우량주매니아", totalAsset: 62210279, profit: 12210279, rate: 24.42 },
        { rank: 5, nickname: "금융자유인", totalAsset: 61974327, profit: 11974327, rate: 23.95 },
        { rank: 6, nickname: "테마주달인", totalAsset: 61959069, profit: 11959069, rate: 23.92 },
        { rank: 7, nickname: "주식왕", totalAsset: 60525761, profit: 10525761, rate: 21.05 },
        { rank: 8, nickname: "월가의늑대", totalAsset: 59272169, profit: 9272169, rate: 18.54 },
    ];

    const rankIcon = (rank) => {
        if (rank === 1) return "🏆";
        if (rank === 2) return "🥈";
        if (rank === 3) return "🥉";
        return rank;
    };

    return (    
        <div className="min-h-screen bg-[#f8fafc] px-6 py-8">
            <div className="mx-auto max-w-4xl">
                {/* 상단 요약 카드 */}
                <section className="rounded-2xl bg-linear-to-br from-blue-500 via-indigo-500 to-purple-600 p-7 text-white shadow-lg">
                <div className="flex items-start justify-between">
                    <div>
                    <p className="text-sm text-white/80">내 순위</p>
                    <p className="mt-1 text-4xl font-light">16위</p>
                    </div>

                    <div className="text-right">
                    <p className="text-sm text-white/80">총 참가자</p>
                    <p className="mt-1 text-2xl font-semibold">20명</p>
                    </div>
                </div>

                <div className="my-6 h-px bg-white/20" />

                <div className="grid grid-cols-2 gap-6">
                    <div>
                    <p className="text-sm text-white/80">총 자산</p>
                    <p className="mt-1 text-xl font-semibold">₩50,000,000</p>
                    </div>

                    <div>
                    <p className="text-sm text-white/80">수익률</p>
                    <p className="mt-1 text-xl font-semibold">↗ +0.00%</p>
                    </div>
                </div>
                </section>

                {/* 랭킹 테이블 */}
                <section className="mt-5 overflow-hidden rounded-2xl border border-gray-100 bg-white shadow-sm">
                <table className="w-full text-sm">
                    <thead className="bg-gray-50 text-gray-500">
                    <tr className="border-b border-gray-100">
                        <th className="px-6 py-4 text-center font-semibold">순위</th>
                        <th className="px-6 py-4 text-left font-semibold">닉네임</th>
                        <th className="px-6 py-4 text-right font-semibold">총 자산</th>
                        <th className="px-6 py-4 text-right font-semibold">수익금</th>
                        <th className="px-6 py-4 text-right font-semibold">수익률</th>
                    </tr>
                    </thead>

                    <tbody>
                    {rankings.map((user) => (
                        <tr
                        key={user.rank}
                        className="border-b border-gray-100 transition last:border-b-0 hover:bg-gray-50"
                        >
                        <td className="px-6 py-4 text-center text-lg">
                            {rankIcon(user.rank)}
                        </td>
                        <td className="px-6 py-4 font-medium text-gray-800">
                            {user.nickname}
                        </td>
                        <td className="px-6 py-4 text-right font-medium text-gray-700">
                            ₩{user.totalAsset.toLocaleString()}
                        </td>
                        <td className="px-6 py-4 text-right font-semibold text-emerald-500">
                            +₩{user.profit.toLocaleString()}
                        </td>
                        <td className="px-6 py-4 text-right font-semibold text-emerald-500">
                            ↗ +{user.rate.toFixed(2)}%
                        </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
                </section>
            </div>
        </div>
    );
};

export default RankingPage;