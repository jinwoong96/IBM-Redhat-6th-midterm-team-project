import { Calendar, Mail, TrendingDown, TrendingUp, User } from 'lucide-react';
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchUser } from '../../Slice/userSlice';
import { fetchMyBalance } from '../../Slice/balanceSlice';
import { updateUser } from '../../Slice/userSlice';
import { CONSTANTS_CONFIG } from '@/config';

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


    const seed_money = CONSTANTS_CONFIG.SEED_MONEY;
    const profitAmount = totalAssets - seed_money; 
    const profitRate = profitAmount / seed_money * 100;


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

    return (<>
            <div className="flex items-center gap-6">
                <div className="flex h-20 w-20 items-center justify-center rounded-full bg-linear-to-br from-blue-500 to-purple-600 text-white">
                    <User size={42} />
                </div>

                <div>
                    <div className="flex items-center gap-3">
                        <h2 className="text-2xl font-semibold text-gray-800">{user_nickname}</h2>
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
                            {formatDate(created_at)}
                        </span>
                    </div>
                </div>
            </div>


            {/* ////////////////////////////////////////////////////////////////// */}
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
            {/* /////////////////////////////////////////////////////// */}

            <div className="my-7 border-t border-gray-100" />

            <div className="grid grid-cols-3 gap-8">
                <div>
                    <p className="text-sm text-gray-500">총 자산</p>
                    <p className="mt-2 text-2xl font-semibold text-gray-900">₩{totalAssets.toLocaleString()}</p>
                </div>
                <div>
                    <p className="text-sm text-gray-500">수익금</p>
                    <p className="mt-2 text-2xl font-semibold text-emerald-500">
                        {profitAmount>=0?"+":""}₩{profitAmount.toLocaleString()}</p>
                </div>
                <div>
                    <p className="text-sm text-gray-500">수익률</p>
                    <div className="mt-2 flex items-center text-2xl font-semibold text-emerald-500">
                        {profitRate>=0?<TrendingUp size={18} />:<TrendingDown size={18} />}
                        <span className="ml-1">
                            {profitRate>=0?" +":" "}
                            {profitRate.toFixed(2)}%
                        </span>
                    </div>
                </div>
            </div>
        </>
    );
};

export default MyInfo;