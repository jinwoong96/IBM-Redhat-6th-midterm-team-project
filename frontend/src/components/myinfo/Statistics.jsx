import { Activity } from 'lucide-react';
import React, {useEffect} from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTrade } from '../../Slice/tradeSlice';
import { fetchUser } from '../../Slice/userSlice';
import StatCard from '../common/StatCard';

const Statistics = () => {

    const dispatch = useDispatch();
    const my_trade = useSelector((state)=> state.trade.trades) || [];
    const {login_id,money,valuation} = useSelector((state)=>state.user);

    useEffect(()=>{
        dispatch(fetchTrade());
        dispatch(fetchUser());
    },[dispatch])
    const totalTradeCount = my_trade.length; 
    const buyCount = my_trade.filter(trade => trade.buy_type === 'buy').length; 
    const sellCount = my_trade.filter(trade => trade.buy_type === 'sell').length;

    return (
        <div>
            <h3 className="flex items-center gap-2 text-xl font-semibold text-gray-800">
                <Activity size={22} className="text-purple-500" />
                거래 통계
            </h3>

            <div className="mt-7 space-y-4">
                <div className="flex items-center justify-between rounded-xl bg-blue-50 px-4 py-4">
                    <span className="text-sm font-medium text-gray-600">총 거래 횟수</span>
                    <span className="text-xl font-semibold text-blue-500">{totalTradeCount}회</span>
                </div>

                <div className="grid grid-cols-2 gap-4">
                    <StatCard label="매수" value={`${buyCount}회`} color="text-emerald-500" bg="bg-emerald-50" />
                    <StatCard label="매도" value={`${sellCount}회`} color="text-red-500" bg="bg-red-50" />
                    <StatCard label="현금보유량" value={`${money?.toLocaleString()}원`} color="text-purple-500" bg="bg-purple-50" />
                    <StatCard label="평가금액" value={`${valuation?.toLocaleString()}원`} color="text-orange-500" bg="bg-orange-50" />
                </div>
            </div>
        </div>
    );
};

export default Statistics;