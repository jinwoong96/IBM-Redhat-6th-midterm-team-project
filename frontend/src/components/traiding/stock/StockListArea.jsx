import React from 'react';
import FilterButtonArea from './FilterButtonArea';
import StockList from './StockList';

const StockListArea = () => {
    return (
        <>
            <div className="border-b border-gray-100 px-4 py-3">
                <div>
                    <div className="inline-block border-b-2 border-blue-500 pb-2 text-sm font-semibold text-blue-600">
                        국내주식
                    </div>
                </div>
                <FilterButtonArea />
            </div>
            <StockList />
        </>
    );
};

export default StockListArea;