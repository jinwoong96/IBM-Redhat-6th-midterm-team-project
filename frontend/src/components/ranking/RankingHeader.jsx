import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchMyRanking } from '../../Slice/rankingSlice';
import { useEffect } from 'react';
const RankingHeader = () => {
    const dispatch = useDispatch();
    const myRanking = useSelector((state) => state.rank.myRanking);
    const all_rank =useSelector((state)=>state.rank.all_rankings);
    useEffect(() => {
        dispatch(fetchMyRanking());
    }, [dispatch]);
    if (!myRanking) {
        return <div>랭킹 데이터를 불러올 수 없습니다. (혹은 로딩 중)</div>;
    }
    return (
        <div style={{ padding: '20px', borderBottom: '1px solid #ccc', backgroundColor: '#f9f9f9' }}>
            <h3>나의 랭킹 요약</h3>
            <div style={{ display: 'flex', gap: '20px' }}>
                <div>
                    <strong>내 순위:</strong> {myRanking.rank}위
                </div>
                <div>
                    <strong>총 참가자 수 :</strong> {all_rank} 명
                </div>
                <div>
                    <strong>최대 잔고:</strong> {myRanking.max_accounts.toLocaleString()}원
                </div>
                <div>
                    <strong>수익률:</strong> 
                    <span style={{ color: myRanking.max_plus >= 0 ? 'red' : 'blue' }}>
                        {myRanking.max_plus}%
                    </span>
                </div>
            </div>
            <p style={{ fontSize: '12px', color: '#666' }}>ID: {myRanking.login_id}</p>
        </div>
    );
};

export default RankingHeader;