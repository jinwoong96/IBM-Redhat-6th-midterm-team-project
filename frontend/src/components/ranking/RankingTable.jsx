import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTopRankings } from '../../Slice/rankingSlice';

const RankingTable = () => {
    const dispatch = useDispatch();
    // 리덕스 스토어에서 전체 랭킹 리스트 가져오기
    const Rankinglist = useSelector((state) => state.rank.topRankings);

    useEffect(() => {
        dispatch(fetchTopRankings());
    }, [dispatch]);


    return (
        <div style={{ marginTop: '20px', width: '100%' }}>
            <h3 style={{ paddingLeft: '15px', color: '#333' }}>전체 랭킹 TOP 10</h3>
            <ul style={{ listStyle: 'none', padding: 0, borderTop: '2px solid #333' }}>
                {Rankinglist.map((user) => (
                    <li 
                        key={user.login_id} 
                        style={{
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            padding: '12px 20px',
                            borderBottom: '1px solid #eee',
                            // 백엔드에서 준 user.rank를 활용해 1, 2, 3위 강조
                            backgroundColor: user.rank <= 3 ? '#fff9db' : 'white'
                        }}
                    >
                        <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
                            {/* 백엔드에서 계산해서 보내준 rank 사용 */}
                            <span style={{ 
                                fontWeight: 'bold', 
                                width: '40px',
                                fontSize: user.rank <= 3 ? '1.2rem' : '1rem',
                                color: user.rank === 1 ? '#f1c40f' : '#333'
                            }}>
                                {user.rank}위
                            </span>
                            
                            <div style={{ display: 'flex', flexDirection: 'column' }}>
                                <span style={{ fontWeight: '600' }}>{user.user_nickname}</span>
                                <span style={{ fontSize: '0.85rem', color: '#888' }}>@{user.login_id}</span>
                            </div>
                        </div>
                        
                        <div style={{ textAlign: 'right' }}>
                            <span style={{ display: 'block', fontSize: '0.9rem', color: '#666' }}>최대 잔고</span>
                            <strong style={{ fontSize: '1.05rem', color: '#2c3e50' }}>
                                {user.max_accounts.toLocaleString()}원
                            </strong>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RankingTable;