import React from 'react';
import RankingRow from './RankingRow';

const RankingTable = () => {
    /////////////// 랭킹 목록 데이터 불러오기
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
    ///////////////////////////////////////////////////////////////////

    return (
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
                <RankingRow user={user} key={user.rank}/>
            ))}
            </tbody>
        </table>
    );
};

export default RankingTable;