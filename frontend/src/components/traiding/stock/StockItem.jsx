import { Star } from 'lucide-react';
import React from 'react';

const StockItem = ({item}) => {

    const onWishClick = (e, item_code, isWish) => {
        // 관심종목 추가/삭제 클릭했을 때
        e.stopPropagation(); // 종목 자체도 클릭 이벤트 있으니까 별 눌렀을 떄는 버블링 방지 넣어줌
        alert("관심종목 추가 또는 삭제");
    }

    const onItemClick = () => {
        alert("종목 클릭하면 해당 종목 차트를 불러와서 띄워줌. 클릭한 종목 active=true로 바꾸고 나머지는 false")
    }

    return (
        <div
            key={item.item_code}
            onClick={()=>onItemClick()}
            className={`flex w-full items-start justify-between px-4 py-4 text-left transition hover:bg-gray-50 ${
                item.active ? "bg-blue-50" : "bg-white"
            }`}
            >
            <div>
                <div className="flex items-center gap-1">
                <span className="font-semibold">{item.item_name}</span>
                <button onClick={(e)=>(onWishClick(e, item.item_code, item.isWish))}>
                    <Star
                        size={14}
                        className={
                            item.isWish
                            ? "fill-yellow-400 text-yellow-400"
                            : "text-gray-300"
                        }
                    />
                </button>
                </div>
                <div className="text-xs text-gray-400">{item.item_code}</div>
                <div className="mt-1 font-semibold">{"₩"+item.price.toLocaleString()}</div>
            </div>

            <div className="flex flex-col items-end gap-2">
                <span
                className={`text-sm font-medium ${
                    item.change>0 ? "text-red-500" : "text-blue-500"
                }`}
                >
                {/* 변동비율은 부호에 따라서 +이면 + 붙여주고, 뒤에 % 붙여주고 소수점 2자리까지 자릿수고정해서 string으로 띄워줌(util 함수 따로 짜서) */}
                {item.change}
                </span>
                <span className="rounded-md bg-gray-100 px-2 py-1 text-xs text-gray-500">
                {item.category}
                </span>
            </div>
        </div>
    );
};

export default StockItem;