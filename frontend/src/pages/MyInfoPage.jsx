import React from 'react';
import { User, Mail, Calendar, PieChart, Activity } from "lucide-react";
import MyInfo from '../components/myinfo/MyInfo';
import Assets from '../components/myinfo/Assets';
import Statistics from '../components/myinfo/Statistics';


const MyInfoPage = () => {

    const cash = 30000000;
    const stock = 20000000;

    const total = cash + stock;

    const cashPercent = total === 0 ? 0 : (cash / total) * 100;
    const stockPercent = total === 0 ? 0 : (stock / total) * 100;

    return (
        <div className="min-h-screen bg-linear-to-br from-blue-50 via-white to-purple-50 px-6 py-8">
        <div className="mx-auto max-w-5xl space-y-6">
            {/* 프로필 카드 */}
            <section className="rounded-2xl border border-gray-100 bg-white p-8 shadow-sm">
            <div className="flex items-center gap-6">
                <div className="flex h-20 w-20 items-center justify-center rounded-full bg-linear-to-br from-blue-500 to-purple-600 text-white">
                <User size={42} />
                </div>

                <div>
                <div className="flex items-center gap-3">
                    <h2 className="text-2xl font-semibold text-gray-800">투자왕</h2>
                    <button className="text-xs font-medium text-blue-500 hover:underline">
                    닉네임 수정
                    </button>
                    <button className="text-xs font-medium text-purple-500 hover:underline">
                    비밀번호 수정
                    </button>
                </div>

                <div className="mt-3 flex items-center gap-5 text-sm text-gray-500">
                    <span className="flex items-center gap-1">
                    <Mail size={16} />
                    test@gmail.com
                    </span>
                    <span className="flex items-center gap-1">
                    <Calendar size={16} />
                    2026년 1월 1일
                    </span>
                </div>
                </div>
            </div>

            <div className="my-7 border-t border-gray-100" />

            <div className="grid grid-cols-3 gap-8">
                <div>
                <p className="text-sm text-gray-500">총 자산</p>
                <p className="mt-2 text-2xl font-semibold text-gray-900">₩50,000,000</p>
                </div>
                <div>
                <p className="text-sm text-gray-500">수익금</p>
                <p className="mt-2 text-2xl font-semibold text-emerald-500">+₩0</p>
                </div>
                <div>
                <p className="text-sm text-gray-500">수익률</p>
                <p className="mt-2 text-2xl font-semibold text-emerald-500">↗ +0.00%</p>
                </div>
            </div>
            </section>

            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
            {/* 자산 구성 */}
            <section className="rounded-2xl border border-gray-100 bg-white p-7 shadow-sm">
                <h3 className="flex items-center gap-2 text-xl font-semibold text-gray-800">
                    자산 구성
                </h3>

                <div className="mt-8 flex justify-center">
                    <div
                    className="relative h-48 w-48 rounded-full"
                    style={{
                        background: `conic-gradient(
                        #3b82f6 0% ${cashPercent}%,
                        #10b981 ${cashPercent}% 100%
                        )`,
                    }}
                    >
                    {/* 가운데 구멍 */}
                    <div className="absolute inset-6 flex items-center justify-center rounded-full bg-white text-sm font-medium shadow">
                        ₩{total.toLocaleString()}
                    </div>
                    </div>
                </div>

                {/* 범례 */}
                <div className="mt-8 space-y-3 text-sm">
                    <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <span className="h-3 w-3 rounded-full bg-blue-500" />
                        현금
                    </div>
                    <span className="text-gray-600">
                        {cashPercent.toFixed(1)}%
                    </span>
                    </div>

                    <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <span className="h-3 w-3 rounded-full bg-emerald-500" />
                        주식
                    </div>
                    <span className="text-gray-600">
                        {stockPercent.toFixed(1)}%
                    </span>
                    </div>
                </div>
            </section>

            {/* 거래 통계 */}
            <section className="rounded-2xl border border-gray-100 bg-white p-7 shadow-sm">
                <h3 className="flex items-center gap-2 text-xl font-semibold text-gray-800">
                    <Activity size={22} className="text-purple-500" />
                    거래 통계
                </h3>

                <div className="mt-7 space-y-4">
                    <div className="flex items-center justify-between rounded-xl bg-blue-50 px-4 py-4">
                        <span className="text-sm font-medium text-gray-600">총 거래 횟수</span>
                        <span className="text-xl font-semibold text-blue-500">0회</span>
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                        <StatCard label="매수" value="0회" color="text-emerald-500" bg="bg-emerald-50" />
                        <StatCard label="매도" value="0회" color="text-red-500" bg="bg-red-50" />
                        <StatCard label="현금보유량" value="0개" color="text-purple-500" bg="bg-purple-50" />
                        <StatCard label="평가금액" value="0원" color="text-orange-500" bg="bg-orange-50" />
                    </div>
                </div>
            </section>
            </div>
        </div>
        </div>
    );
    };

    const StatCard = ({ label, value, color, bg }) => {
    return (
        <div className={`rounded-xl ${bg} px-4 py-4`}>
        <p className="text-sm font-medium text-gray-500">{label}</p>
        <p className={`mt-2 text-xl font-semibold ${color}`}>{value}</p>
        </div>
    );
};

export default MyInfoPage;