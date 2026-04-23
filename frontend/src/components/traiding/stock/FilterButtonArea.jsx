import React, { useState } from 'react';

const FilterButtonArea = () => {
    const filterItems = ["전체", "관심종목", "카테고리", "등락폭별"];

    // 이건 스토어에 저장해야될듯?
    const [selectedStockFilter, setSelectedStockFilter] = useState("전체");

    return (
        <div className="flex flex-wrap gap-2 py-3">
            {filterItems.map((item) => (
                <button
                    key={item}
                    onClick={()=>setSelectedStockFilter(item)}
                    className={`rounded-full px-3 py-1 text-xs font-medium ${
                        item===selectedStockFilter
                        ? "bg-blue-100 text-blue-600"
                    : "bg-gray-100 text-gray-500 hover:bg-gray-200"
                    }`}
                    >
                    {item}
                </button>
            ))}

        </div>
    );
};

export default FilterButtonArea;