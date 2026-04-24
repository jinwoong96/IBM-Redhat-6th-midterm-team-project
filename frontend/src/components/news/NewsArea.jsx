import React, { useState } from 'react';
import NewsCard from './NewsCard';

const NewsArea = () => {
    ////////////////// 뉴스 데이터 가져오기. 가져올 때 setCurrentIndex (제일 최근뉴스로) ///////////////////////////
    const newsList = [
        {
        day: "1",
        title: "NVIDIA, 혁신적인 AI 칩 공개",
        comment: "NVIDIA가 차세대 인공지능 칩을 공개하며 시장 기대감이 높아지고 있습니다.",
        },
        {
        day: "2",
        title: "반도체 업종 강세",
        comment: "글로벌 반도체 수요 회복 기대감으로 관련 종목들이 상승하고 있습니다.",
        },
        {
        day: "3",
        title: "전기차 배터리 투자 확대",
        comment: "주요 기업들이 배터리 생산 시설 투자를 확대하고 있습니다.",
        },
    ];
    /////////////////////////////////////////////////////////////////////////////////

    const [currentIndex, setCurrentIndex] = useState(0);

    const currentNews = newsList[currentIndex];

    const prevNews = () => {
        setCurrentIndex((prev) =>
            prev === 0 ? newsList.length - 1 : prev - 1
        );
    };

    const nextNews = () => {
        setCurrentIndex((prev) =>
            prev === newsList.length - 1 ? 0 : prev + 1
        );
    };


    return (
        <div className="mt-4 rounded-3xl border border-gray-200 bg-[#fafafa] p-4">
            <div className="flex items-center gap-4">
                {/* 왼쪽 화살표 */}
                <button
                    type="button"
                    onClick={prevNews}
                    className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-white text-xl shadow-sm hover:bg-gray-100"
                >
                ‹
                </button>

                {/* 뉴스 카드 */}
                <NewsCard currentNews={currentNews} currentIndex={currentIndex} length={newsList.length}/>

                {/* 오른쪽 화살표 */}
                <button
                    type="button"
                    onClick={nextNews}
                    className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-white text-xl shadow-sm hover:bg-gray-100"
                >
                ›
                </button>
            </div>
        </div>
    );
};

export default NewsArea;