import React from 'react';
import { Link } from 'react-router-dom';
import NavButton from '../common/NavButton';
import NavCard from '../common/NavCard';
const IntroNav = () => {
    {/* 초기화면 네비바 */}
    return (
        <>
            <div className="mt-16 grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                <NavCard to="/a" icon={"🎯"} text={"트레이드"}/>
                <NavCard to="/b" icon={"🏅"} text={"랭킹"}/>
            </div>
            <div className="mt-10 flex justify-center gap-6">
                <NavButton to="/c" text={"로그인"} />
                <NavButton to="/d" text={"회원가입"} />
            </div>
        </>
    );
};

export default IntroNav;