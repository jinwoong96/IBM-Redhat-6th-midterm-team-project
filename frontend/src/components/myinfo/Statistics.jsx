import React, {useEffect} from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTrade } from '../../Slice/tradeSlice';
import { fetchUser } from '../../Slice/userSlice';

const Statistics = () => {
    const dispatch = useDispatch();
    const my_trade = useSelector((state)=> state.trade.trades) || [];
    const {login_id,money,valuation} = useSelector((state)=>state.user);

    useEffect(()=>{
        dispatch(fetchTrade());
        dispatch(fetchUser());
    },[dispatch])
    const totalTradeCount = my_trade.length; 
    const buyCount = my_trade.filter(trade => trade.buy_type === 'buy').length; 
    const sellCount = my_trade.filter(trade => trade.buy_type === 'sell').length;
    return (
        <div>
            <h3>거래 및 자산 통계</h3>

            <section>
                <h4>거래 현황</h4>
                <div>
                    <p>총 거래: <strong>{totalTradeCount}건</strong></p>
                    <p>매수: <strong>{buyCount}건</strong></p>
                    <p>매도: <strong>{sellCount}건</strong></p>
                </div>
            </section>

            <hr />

            <section>
                <h4>자산 비중</h4>
                <div>
                    <p>현금 보유량: <strong>₩ {money?.toLocaleString()}</strong></p>
                    <p>평가 금액: <strong>₩ {valuation?.toLocaleString()}</strong></p>
                </div>
            </section>
        </div>
    );
};

export default Statistics;