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
import { fetchMyBalance } from '../../Slice/balanceSlice';
import NewsModal from '../modal/NewsModal';
import { fetchNewsUser } from '../../Slice/newsuserSlice';
const HeaderBar = () => {
    const [isSettlementOpen, setIsSettlementOpen] = useState(false);
    const [isNewsOpen, setIsNewsOpen] = useState(false);
    const data = useSelector((state) => state.progress.next_data);
    const success = useSelector((state)=>state.progress.next_turn);
    const hasDay = data?.day !== undefined && data?.day !== null && !isNaN(Number(data?.day))
    ? Number(data.day): 1; 
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleNewsClose = async() => {
        await dispatch(fetchNewsUser()); // 뉴스 모달 확인 클릭시 뉴스 리스트 최신업데이트
        setIsNewsOpen(false);
    }

    const handleSettlementClose = async() => { 
        await dispatch(resetNextTurn());
        await dispatch(fetchMyBalance()); // 날짜 넘기기 클릭시 내 잔고 업데이트
        setIsSettlementOpen(false);
        setIsNewsOpen(true);
        
    };

    const onTradingClick = () => {
        navigate('/trading');
    }

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

    useEffect(()=>{
       dispatch(fetchProgress()); //새로고침하면 day 1일로 초기화되는거 계속 현재 날짜 가져와야함
    },[])

    return (
        <div>
            <header className="flex items-center justify-between border-b border-gray-200 bg-white px-6 py-3">
                <div className="flex items-center gap-4">
                    <h1 className="text-xl font-bold" onClick={()=>navigate('/trading')}>모의 주식 투자</h1>
                    {/*모의 주식 투자 글씨 클릭시 트레이딩화면 가기 */}
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
            <NewsModal 
                isOpen={isNewsOpen}
                onClose={handleNewsClose}
                isNewsOpen = {isNewsOpen}
            />    
        </div>
    );
};

export default HeaderBar;