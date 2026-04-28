import React, { useState, useEffect } from 'react';
import StockListArea from '../components/traiding/stock/StockListArea';
import ChartArea from '../components/traiding/stockchart/ChartArea';
import NewsArea from '../components/news/NewsArea';
import AccountSummary from '../components/traiding/account/AccountSummary';
import BalanceSummary from '../components/traiding/account/BalanceSummary';
import TradePanel from '../components/traiding/trade/TradePanel';
import HistoryArea from '../components/traiding/HistoryArea';
import NewsModal from '../components/modal/NewsModal';
import { useDispatch, useSelector } from 'react-redux';
import { fetchNews_last, fetchNewsUser, setNewsChecked } from '../Slice/newsuserSlice';
import { resetLastNews } from '../Slice/newsuserSlice';
import { useNavigate } from 'react-router-dom';
const TradingPage = () => {
    const [isNewsOpen, setIsNewsOpen] = useState(false);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const last_news = useSelector((state) => state.newsuser.last_news);    
    const news_checked = useSelector((state) => state.newsuser.news_checked); 
    const user = useSelector((state)=>state.user.login_id)   
    useEffect(() => {
        const loadNews = async () => {
            await dispatch(fetchNews_last()); // 최신 뉴스 가져오기
            if (!user) {
                await alert("로그인하세요!!!!!!!!!!!!!!!!!!!")
                navigate("/")
            }

        };
        loadNews();
    }, []);

    useEffect(() => {
        if (last_news && !news_checked) {  
            setIsNewsOpen(true);
        }
    }, [last_news, news_checked]);
    const handleNewsClose = async () => {
        await dispatch(fetchNewsUser());
        await dispatch(setNewsChecked());
        await dispatch(resetLastNews())
        setIsNewsOpen(false);
    };    
    return (
        <div className="grid grid-cols-12 gap-4 px-4 py-3">
            <section className="col-span-12 lg:col-span-2 overflow-hidden rounded-2xl border border-gray-200 bg-white">
                <StockListArea />
            </section>
            <section className="col-span-12 lg:col-span-8 min-w-0 space-y-4 flex flex-col">
                <ChartArea />
                <NewsArea />
                <HistoryArea />
            </section>
            <section className="col-span-12 lg:col-span-2 min-w-0 space-y-4">
                <AccountSummary />
                <BalanceSummary />
                <TradePanel />
                {/* <HistoryArea /> */}
            </section>
            {/* ✅ 뉴스 모달 */}
            <NewsModal
                
                isNewsOpen={isNewsOpen}
                onClose={handleNewsClose}
            />
        </div>
        
    );
};

export default TradingPage;