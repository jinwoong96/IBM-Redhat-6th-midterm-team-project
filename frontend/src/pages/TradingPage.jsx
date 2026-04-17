import React from 'react';
import StockList from '../components/traiding/stock/StockList';
import ChartArea from '../components/traiding/stockchart/ChartArea';
import NewsArea from '../components/news/NewsArea';

const TradingPage = () => {
    return (
        <div className="grid grid-cols-12 gap-4">
            <section className="col-span-2"><StockList /></section>
            <section className="col-span-8">
                <ChartArea />
                <NewsArea />
            </section>
            <section className="col-span-2">거래</section>
        </div>
    );
};

export default TradingPage;