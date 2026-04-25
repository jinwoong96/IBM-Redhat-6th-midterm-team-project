import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchMyBalance } from './../../../Slice/balanceSlice';

const BalanceList = () => {
    const dispatch = useDispatch();
    const mybalance = useSelector((state) => state.balance.my_balance);

    useEffect(() => {
        dispatch(fetchMyBalance());
    }, [dispatch]);
    const balanceList = Array.isArray(mybalance) ? mybalance : [];

    return (
        <div>
            <h3>나의 잔고 현황</h3>
            <hr />
            {balanceList.length > 0 ? (
                balanceList.map((item, index) => {
                    const isPositive = item.val_profit_and_loss >= 0;
                    const color = isPositive ? 'red' : 'blue';

                    return (
                        <div key={item.item_code || index}>
                            <div>
                                <strong>{item.item_name} ({item.item_code})</strong>
                            </div>
                            <div>
                                <span>보유수량: {item.quantity}주 | </span>
                                <span>총 구매가: {item.purchase_price?.toLocaleString()}원</span>
                            </div>
                            <div>
                                <span>평가금액: {item.val_price?.toLocaleString()}원</span>
                            </div>
                            <div style={{ color: color }}>
                                <span>평가손익: {item.val_profit_and_loss?.toLocaleString()}원 </span>
                                <span>({item.rate_of_return?.toFixed(2)}%)</span>
                            </div>
                            <hr style={{ borderTop: '1px dashed #ccc' }} />
                        </div>
                    );
                })
            ) : (
                <p>보유 중인 종목이 없습니다.</p>
            )}
        </div>
    );
};

export default BalanceList;