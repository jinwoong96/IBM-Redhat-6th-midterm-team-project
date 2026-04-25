import React, { useState } from 'react';
import NewsCard from './NewsCard';

const NewsArea = () => {
    const dispatch = useDispatch();
    const newsList = useSelector((state)=>state.newsuser.newslist)

    useEffect(()=>{
        dispatch(fetchNewsUser());
    },[dispatch])
    
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