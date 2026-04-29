import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchMyBalance } from './../../../Slice/balanceSlice';
import { fetchChart_code } from '../../../Slice/chartuserSlice';

const BalanceList = () => {
    const dispatch = useDispatch();
    const mybalance = useSelector((state) => state.balance.my_balance);

    useEffect(() => {
        dispatch(fetchMyBalance());
    }, [dispatch]);
    const balances = Array.isArray(mybalance) ? mybalance : [];

    return (
        <div className="max-h-[25vh] overflow-y-auto">
            <table className="w-full text-sm table-fixed border-collapse">
                <thead className="sticky top-0 z-10 bg-gray-50 text-gray-600">
                    <tr className="border-b border-gray-100">
                        <th className="px-2 py-2 text-center border-r border-gray-100">종목코드</th>
                        <th className="px-2 py-2 text-center border-r border-gray-100">종목명</th>
                        <th className="px-2 py-2 text-center border-r border-gray-100">수량</th>
                        <th className="px-2 py-2 text-center border-r border-gray-100">매입단가</th>
                        <th className="px-2 py-2 text-center border-r border-gray-100">평가금액</th>
                        <th className="px-2 py-2 text-center border-r border-gray-100">평가손익</th>
                        <th className="px-2 py-2 text-center">수익률</th>
                    </tr>
                </thead>

                <tbody>
                    {balances.map((item, index) => (
                        <tr
                            key={index}
                            className="border-b border-gray-100 hover:bg-gray-50 cursor-pointer"
                            onClick={() => dispatch(fetchChart_code(item.item_code))}
                        >
                            <td className="px-2 py-2 border-r border-gray-100">{item.item_code}</td>
                            <td className="px-2 py-2 border-r border-gray-100 truncate">{item.item_name}</td>
                            <td className="px-2 py-2 text-right border-r border-gray-100">{item.quantity}</td>
                            <td className="px-2 py-2 text-right border-r border-gray-100">{(Math.floor(item.purchase_price/item.quantity)).toLocaleString()}</td>
                            <td className={`px-2 py-2 text-right font-medium border-r border-gray-100 ${
                                    item.val_profit_and_loss > 0
                                        ? "text-red-500"
                                        : item.val_profit_and_loss < 0
                                        ? "text-blue-500"
                                        : "text-gray-500"
                                }`}>{item.val_price.toLocaleString()}</td>

                            <td
                                className={`px-2 py-2 text-right font-medium border-r border-gray-100 ${
                                    item.val_profit_and_loss > 0
                                        ? "text-red-500"
                                        : item.val_profit_and_loss < 0
                                        ? "text-blue-500"
                                        : "text-gray-500"
                                }`}
                            >
                                {item.val_profit_and_loss > 0 ? "+" : ""}
                                {item.val_profit_and_loss.toLocaleString()}
                            </td>

                            <td
                                className={`px-2 py-2 text-right font-medium ${
                                    item.rate_of_return > 0
                                        ? "text-red-500"
                                        : item.rate_of_return < 0
                                        ? "text-blue-500"
                                        : "text-gray-500"
                                }`}
                            >
                                {item.rate_of_return > 0 ? "+" : ""}
                                {item.rate_of_return.toFixed(2)}%
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default BalanceList;