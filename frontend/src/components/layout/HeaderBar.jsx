import React, { useState } from 'react';
import { User } from "lucide-react";
import DayBadge from '../common/DayBadge';
import MenuButton from '../common/MenuButton';
import { useNavigate } from 'react-router-dom';
import IconMenuButton from '../common/IconMenuButton';

const HeaderBar = () => {
    // 날짜랑 set함수는 컨텍스트나 저장소에서 받아오고 이거 지우기
    const [day, setDay] = useState(1);

    const navigator = useNavigate();

    const onTradingClick = () => {
        alert("/components/layout/HeaderBar.jsx 코드 짜기\n게임 페이지 코드 다 되면 setDay랑 주석 지우기");
        setDay(1);

        navigator('/trading');
    }

    const onNextDayClick = () => {
        alert("/components/layout/HeaderBar.jsx 코드 짜기\n일차 변하는것도 불러와서 넣어주기")
    }

    const onRankingClick = () => {
        setDay(null);
        navigator('/ranking');
    }

    const onLogoutClick = () => {
        setDay(null);
        alert("/components/layout/HeaderBar.jsx 코드 짜기")
    }

    return (
        <div>
            <header className="flex items-center justify-between border-b border-gray-200 bg-white px-6 py-3">
                <div className="flex items-center gap-4">
                    <h1 className="text-xl font-bold">모의 주식 투자</h1>
                    {day?<DayBadge content={`day ${day}`} />:<></>}
                </div>

                <div className="flex items-center gap-3">
                    {day?<MenuButton content={"날짜 넘기기"} onClick={()=>onNextDayClick()} />
                    :<MenuButton content={"트레이딩"} onClick={()=>onTradingClick()}/>}
                    
                    <MenuButton content={"랭킹"} onClick={()=>onRankingClick()} />
                    <IconMenuButton content={<User size={16}/>} onClick={()=>navigator('/myinfo')}/>
                    <MenuButton content={"로그아웃"} onClick={()=>onLogoutClick()} />
                </div>
            </header>
        </div>
    );
};

export default HeaderBar;