import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchUser } from '../../Slice/userSlice';
import { fetchMyBalance } from '../../Slice/balanceSlice';
import { updateUser } from '../../Slice/userSlice';
const MyInfo = () => {
    const dispatch = useDispatch();

    const { money, user_nickname, login_id, created_at } = useSelector((state) => state.user);
    const { my_balance } = useSelector((state) => state.balance);

    const [isEdit, setIsEdit] = useState(false);
    const [editNickname, setEditNickname] = useState("");
    const [editPassword, setEditPassword] = useState("");
    useEffect(() => {
        dispatch(fetchUser());
        dispatch(fetchMyBalance());
    }, [dispatch]);
    if (!login_id) {
            return <div>사용자 정보를 불러오는 중입니다...</div>;
    }

    const safeBalance = Array.isArray(my_balance) ? my_balance : [];
    const totalStockValue = safeBalance.reduce((acc, cur) => acc + (cur.val_price || 0), 0);
    const totalAssets = (money || 0) + totalStockValue;


    const initialSeed = 50000000;
    const profitAmount = totalAssets - initialSeed; 
    const profitRate = ((totalAssets / initialSeed - 1) * 100).toFixed(2);


    const formatDate = (dateString) => {
        if (!dateString) return "정보 없음";
        const date = new Date(dateString);
        const yy = String(date.getFullYear()).slice(-2); 
        const mm = date.getMonth() + 1;
        const dd = date.getDate();
        return `${yy}년 ${mm}월 ${dd}일`;
    };
    const handleEditClick = () => {
        if (isEdit) {
            
            dispatch(updateUser({ 
                user_nickname: editNickname, 
                user_password: editPassword 
            }));
            setIsEdit(false);
            setEditPassword(""); 
        } else {
            setIsEdit(true);
        }
    };
    return (
        <div>
            <div>
                {isEdit ? (
                    <div style={{ marginBottom: '10px' }}>
                        <input 
                            type="text" 
                            value={editNickname} 
                            onChange={(e) => setEditNickname(e.target.value)}
                            placeholder="새 닉네임"
                        />
                        <input 
                            type="password" 
                            value={editPassword} 
                            onChange={(e) => setEditPassword(e.target.value)}
                            placeholder="새 비밀번호"
                        />
                    </div>
                ) : (
                    <h2>{user_nickname} ({login_id})님</h2>
                )}
                
                <p>계좌 생성일: {formatDate(created_at)}</p>
                <button type="button" onClick={handleEditClick}>
                    {isEdit ? "수정 완료" : "내 정보 수정"}
                </button>
                {isEdit && <button onClick={() => setIsEdit(false)}>취소</button>}
            </div>

            <hr />

            <div>
                <div>
                    <p>총 자산</p>
                    <strong>₩ {totalAssets.toLocaleString()}</strong>
                </div>
                
                <div>
                    <p>수익금</p>
                    <strong>₩ {profitAmount.toLocaleString()}</strong>
                </div>

                <div>
                    <p>수익률</p>
                    <strong>
                        {profitRate >= 0 ? "↗" : "↘"} 
                        {profitRate > 0 ? `+${profitRate}` : profitRate}%
                    </strong>
                </div>
            </div>
        </div>
    );
};

export default MyInfo;