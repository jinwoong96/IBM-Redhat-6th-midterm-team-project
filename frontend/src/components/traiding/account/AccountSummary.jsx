import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchUser } from '../../../Slice/userSlice';

const AccountSummary = () => {
    const dispatch = useDispatch();
    const { money, valuation } = useSelector((state) => state.user);
    const initialInvestment = 50000000;
    // 수익을 전날 대비 수익으로 할건지 정해야함 
    // Progress 할때 전날 money 저장하면 되긴될듯?
    const profit = money+valuation - initialInvestment;


    const profitRate = (((money+valuation) / initialInvestment) - 1) * 100;

    useEffect(() => {
        dispatch(fetchUser());
    }, [dispatch]);

    return (
        <div>
            <h2>계좌 요약</h2>
            <div>
                <p>총 자산: {(money+valuation)?.toLocaleString()}원</p>
                <p>수익: {profit?.toLocaleString()}원</p>
                <p>수익률: {profitRate?.toFixed(2)}%</p>
            </div>
        </div>
    );
};

export default AccountSummary;