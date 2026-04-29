import React, { useState } from 'react';

const FilterButtonArea = ({selectedStockFilter, setSelectedStockFilter}) => {
    const filterItems = ["전체", "가나다순", "관심종목", "카테고리순", "등락폭순"];

    return (
        <div className="flex flex-wrap gap-2 py-3">
            {filterItems.map((item) => (
                <button
                    key={item}
                    onClick={()=>setSelectedStockFilter(item)}
                    className={`rounded-full px-3 py-1 text-xs font-medium cursor-pointer ${
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