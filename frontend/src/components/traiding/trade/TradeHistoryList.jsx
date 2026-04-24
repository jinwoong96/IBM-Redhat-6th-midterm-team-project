import React from 'react';

const TradeHistoryList = () => {
    //////////////////// 체결내역 목록 데이터 불러오기
    const trades = [
        {
        trade_day: 1,
        item_name: "삼성전자",
        buy_type: "buy",
        price: 70000,
        quantity: 10,
        },
    ];
    //////////////////////////////////////////////

    return (
        <div className="h-full overflow-auto">
            <table className="w-full text-sm">
                <thead className="sticky top-0 bg-gray-50 text-gray-600">
                <tr className="border-b border-gray-100">
                    <th className="px-2 py-2 text-center border-r border-gray-100">일차</th>
                    <th className="px-2 py-2 text-center border-r border-gray-100">종목명</th>
                    <th className="px-2 py-2 text-center border-r border-gray-100">구분</th>
                    <th className="px-2 py-2 text-center border-r border-gray-100">가격</th>
                    <th className="px-2 py-2 text-center ">수량</th>
                </tr>
                </thead>

                <tbody>
                {trades.map((item, index) => (
                    <tr key={index} className={`border-b border-gray-100 hover:bg-gray-50 
                                    ${item.buy_type === "buy" ? "text-red-500" : "text-blue-500"}`}>
                    <td className="px-2 py-2 text-right border-r border-gray-100">{item.trade_day}</td>
                    <td className="px-2 py-2 border-r border-gray-100">{item.item_name}</td>
                    <td className="px-2 py-2 border-r border-gray-100">
                        {item.buy_type === "buy" ? "매수" : "매도"}
                    </td>
                    <td className="px-2 py-2 text-right border-r border-gray-100">{item.price.toLocaleString()}</td>
                    <td className="px-2 py-2 text-right">{item.quantity}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
};

export default TradeHistoryList;