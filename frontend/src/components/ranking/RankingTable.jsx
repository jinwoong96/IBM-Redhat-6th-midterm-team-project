import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTopRankings } from '../../Slice/rankingSlice';

const RankingTable = () => {
    const dispatch = useDispatch();
    const Rankinglist = useSelector((state) => state.rank.topRankings);

    useEffect(() => {
        dispatch(fetchTopRankings());
    }, [dispatch]);

    const baseMoney = 2000000;  // 더미데이터 저격 임시

    return (
        <div>
            <h3>전체 랭킹 TOP 10</h3>
            <ol>
                {Rankinglist.map((user) => {
                    const profitAmount = user.max_accounts - baseMoney;
                    const profitRate = ((user.max_accounts / baseMoney - 1) * 100).toFixed(2);

                    return (
                        <li key={user.login_id}>
                            <span>순위: {user.rank}위 </span>
                            <span>닉네임: {user.user_nickname} ({user.login_id}) </span>
                            <span>총자산: {user.max_accounts.toLocaleString()}원 </span>
                            <span>수익금: {profitAmount.toLocaleString()}원 </span>
                            <span>수익률: {profitRate}%</span>
                        </li>
                    );
                })}
            </ol>
        </div>
    );
};

export default RankingTable;