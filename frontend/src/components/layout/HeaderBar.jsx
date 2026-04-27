import React, { useState, useEffect } from 'react';
import { User } from "lucide-react";
import DayBadge from '../common/DayBadge';
import MenuButton from '../common/MenuButton';
import { useNavigate } from 'react-router-dom';
import IconMenuButton from '../common/IconMenuButton';
import { logout } from '../../Slice/userSlice';
import { useSelector, useDispatch } from 'react-redux';
import { fetchNextTurn, fetchProgress, resetNextTurn } from '../../Slice/progressSlice';
import SettlementModal from '../modal/SettlementModal';

const HeaderBar = () => {
    const [isSettlementOpen, setIsSettlementOpen] = useState(false);
    const data = useSelector((state) => state.progress.next_data);
    const success = useSelector((state)=>state.progress.next_turn);
    const hasDay = data?.day !== undefined && data?.day !== null && !isNaN(Number(data?.day))
    ? Number(data.day): 1; 
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const onTradingClick = () => {
        alert("/components/layout/HeaderBar.jsx 코드 짜기\n게임 페이지 코드 다 되면 setDay랑 주석 지우기");

        navigate('/trading');
    }
    const handleSettlementClose = async() => { 
        await dispatch(resetNextTurn());
        setIsSettlementOpen(false);
        
    };

    const onNextDayClick = async() => {
       await dispatch(fetchNextTurn());
        setIsSettlementOpen(true);
        
    }

    const onRankingClick = () => {
        navigate('/ranking');
    }

    const onLogoutClick = async() => {
        await dispatch(logout());
        
        alert("로그아웃 되었습니다.");
        navigate('/login');
    }

    return (
        <div>
            <header className="flex items-center justify-between border-b border-gray-200 bg-white px-6 py-3">
                <div className="flex items-center gap-4">
                    <h1 className="text-xl font-bold">모의 주식 투자</h1>
                    {(hasDay)?<DayBadge content={`day ${(hasDay)}`} />:<></>}
                </div>

                <div className="flex items-center gap-3">
                    {(hasDay)?<MenuButton content={"날짜 넘기기"} onClick={()=>onNextDayClick()} />
                    :<MenuButton content={"트레이딩"} onClick={()=>onTradingClick()}/>}
                    
                    <MenuButton content={"랭킹"} onClick={()=>onRankingClick()} />
                    <IconMenuButton content={<User size={16}/>} onClick={()=>navigate('/myinfo')}/>
                    <MenuButton content={"로그아웃"} onClick={()=>onLogoutClick()} />
                </div>
            </header>
            <SettlementModal
                isOpen={isSettlementOpen}
                day={hasDay}
                success = {success}
                onClose={handleSettlementClose}
            />
        </div>
    );
};

export default HeaderBar;