import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchMyBalance } from '../../../Slice/balanceSlice';
import { fetchUser } from '../../../Slice/userSlice'
import { useEffect } from 'react';
const BalanceSummary = () => {
    const dispatch = useDispatch();
    const mybalance = useSelector((state)=> state.balance);
    const user = useSelector((state)=>state.user);

    useEffect(() => {
        dispatch(fetchMyBalance());
        dispatch(fetchUser());
    }, [dispatch]);

    const totalPrice = (mybalance.my_balance || []).reduce((acc, cur) => {
        return acc + (Number(cur.val_price) || 0);
    }, 0);
    return (
        <div>
            <div>보유 현금, 주식 평가액</div>
            보유 현금 : {user.money?.toLocaleString()}원
            주식 평가액 : {totalPrice?.toLocaleString()}원
        </div>
    );
};

export default BalanceSummary;