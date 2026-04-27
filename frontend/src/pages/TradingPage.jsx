import React, { useState } from 'react';
import StockListArea from '../components/traiding/stock/StockListArea';
import ChartArea from '../components/traiding/stockchart/ChartArea';
import NewsArea from '../components/news/NewsArea';
import AccountSummary from '../components/traiding/account/AccountSummary';
import BalanceSummary from '../components/traiding/account/BalanceSummary';
import TradePanel from '../components/traiding/trade/TradePanel';
import HistoryArea from '../components/traiding/HistoryArea';
import SettlementModal from '../components/modal/SettlementModal';


const TradingPage = () => {

    const [isSettlementOpen, setIsSettlementOpen] = useState(false);
    const currentDay = 1;

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
            <button onClick={() => setIsSettlementOpen(true)}>
                날짜 넘기기
            </button>
            <SettlementModal
                isOpen={isSettlementOpen}
                onClose={() => setIsSettlementOpen(false)}
                day={currentDay}
            />
        </div>
        
    );
};

export default TradingPage;