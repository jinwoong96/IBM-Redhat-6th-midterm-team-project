import React from 'react';
import RankingTable from '../components/ranking/RankingTable';
import RankingHeader from '../components/ranking/RankingHeader';
const RankingPage = () => {

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