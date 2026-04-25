import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchUser } from '../../Slice/userSlice';
import { fetchMyBalance } from '../../Slice/balanceSlice';

const Assets = () => {
    const dispatch = useDispatch();

    const { login_id, money } = useSelector((state) => state.user);
    //const { my_balance } = useSelector((state) => state.balance);
    const my_balance =  [  // 임시 테스트 데이터
            {
                login_id: "qwe",
                item_code: "005930",
                quantity: 5,
                purchase_price: 300000,
                val_price: 400000,
                val_profit_and_loss: 100000,
                rate_of_return: 33
            }
        ]
    useEffect(() => {
        dispatch(fetchUser());
        dispatch(fetchMyBalance());
    }, [dispatch]);

    const filteredBalance = Array.isArray(my_balance) ? my_balance:[];
    const totalStockValue = filteredBalance.reduce((acc, cur) => {
        return acc + (cur.val_price || 0);
    }, 0);

    const totalAssets = (money || 0) + totalStockValue;

    return (
        <div>
            <h3>자산 구성</h3>
            <hr />
            
            <div>
                <p>보유 현금: {money?.toLocaleString()}원</p>
                <p>주식 평가금: {totalStockValue.toLocaleString()}원</p>
                <p><strong>총 자산: {totalAssets.toLocaleString()}원</strong></p>
            </div>

            <hr />

            <div>
                <p>현금 비중: {totalAssets > 0 ? ((money / totalAssets) * 100).toFixed(1) : 0}%</p>
                <p>주식 비중: {totalAssets > 0 ? ((totalStockValue / totalAssets) * 100).toFixed(1) : 0}%</p>
            </div>

            {filteredBalance.length > 0 && (
                <div style={{ marginTop: '10px', fontSize: '0.9rem' }}>
                    <p>[세부 주식 현황]</p>
                    {filteredBalance.map((item, idx) => (
                        <div key={idx}>
                            {item.item_code}: {item.quantity}주 (평가금: {item.val_price?.toLocaleString()}원)
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Assets;