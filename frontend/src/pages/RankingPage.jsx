import React, { useEffect } from 'react';
import RankingTable from '../components/ranking/RankingTable';
import RankingHeader from '../components/ranking/RankingHeader';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
const RankingPage = () => {
    const user = useSelector((state)=>state.user.login_id)
    const navigate = useNavigate();
    useEffect(() => {
        const check = async () => {
            if (!user) { 
            alert("로그인하세요!");
            navigate("/");
            }
        };
        check();
    }, [user]);

    return (    
        <div className="min-h-screen bg-[#f8fafc] px-6 py-8">
            <div className="mx-auto max-w-4xl">
                {/* 상단 요약 카드 */}
                <section className="rounded-2xl bg-linear-to-br from-blue-500 via-indigo-500 to-purple-600 p-7 text-white shadow-lg">
                    <RankingHeader />
                </section>
                {/* 랭킹 테이블 */}
                <section className="mt-5 overflow-hidden rounded-2xl border border-gray-100 bg-white shadow-sm">
                    <RankingTable />
                </section>
            </div>
        </div>
    );
};

export default RankingPage;