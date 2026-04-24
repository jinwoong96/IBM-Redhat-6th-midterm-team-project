import { TrendingDown, TrendingUp } from 'lucide-react';
import React from 'react';

const RankingRow = ({user}) => {

    const rankIcon = (rank) => {
        if (rank === 1) return "🏆";
        if (rank === 2) return "🥈";
        if (rank === 3) return "🥉";
        return rank;
    };

    return (
        <tr
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
                {user.profit>=0?"+":""}₩{user.profit.toLocaleString()}
            </td>
            <td className="flex px-6 py-4 text-right font-semibold text-emerald-500">
                {user.rate>=0?(
                    <TrendingUp size={18} className="text-emerald-500" />
                    ) :
                    <TrendingDown size={18} className="text-emerald-500" />
                    } 
                <span>{user.rate>=0?"+":null}{user.rate.toFixed(2)}%</span>
            </td>
        </tr>
    );
};

export default RankingRow;