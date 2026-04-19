import React, { useState } from 'react';
import TradeHistoryList from './trade/TradeHistoryList';
import BalanceList from './account/BalanceList';

const HistoryArea = () => {
    const [isTradeHistory, setIsTradeHistory] = useState(false);

    return (
        <div>
            <div>
                <button onClick={()=>setIsTradeHistory(false)}>잔고</button>
                <button onClick={()=>setIsTradeHistory(true)}>체결내역</button>
            </div>
            <div>
                {isTradeHistory?<TradeHistoryList />
                :<BalanceList />}
            </div>
        </div>
    );
};

export default HistoryArea;