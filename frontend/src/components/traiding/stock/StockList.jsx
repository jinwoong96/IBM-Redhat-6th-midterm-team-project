import React from 'react';
import StockItem from './StockItem';

const StockList = () => {
    
    // store에서 itemList 가져옴
    // 종목명(item_name), 종목코드(item_code), 현재 가격(전일종가)(price?), 등락율(전일 대비)(change?), 카테고리(category), 관심종목 여부(isWish?), 현재 선택된 상태인가(active?)
    // const itemList = [];
    // active : 종목 목록에서 클릭하면 active가 true로 추가되거나 true로 바뀜. 나머지 종목의 active는 사라지거나 false로 바뀜
    const itemList = [
        { item_name: "네이버", item_code: "035420", price: 185000, change: -0.54, category: "인터넷", isWish: false },
        { item_name: "삼성전자", item_code: "005930", price: 71500, change: 1.42, category: "전자", isWish: true, active: true },
        { item_name: "카카오", item_code: "035720", price: 47500, change: 1.25, category: "인터넷", isWish: true },
        { item_name: "현대자동차", item_code: "005380", price: 225000, change: 0.89, category: "자동차", isWish: false },
        { item_name: "LG화학", item_code: "051910", price: 385000, change: 1.58, category: "화학", isWish: false },
        { item_name: "SK하이닉스", item_code: "000660", price: 145000, change: 2.11, category: "반도체", isWish: true },
    ];

    return (
        <div>
            <div className="border-b border-gray-100 px-4 py-3 text-sm font-semibold text-gray-700">
                종목 리스트 ({itemList.length})
            </div>
            <div className="divide-y divide-gray-100">
                {itemList.map((item) => (<div key={item.item_code}>
                        <StockItem item={item} />
                    </div>
                ))}
          </div>
        </div>
    );
};

export default StockList;