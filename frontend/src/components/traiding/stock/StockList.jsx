import React, { useEffect, useState } from 'react'; 
import { useSelector, useDispatch } from 'react-redux';
import { fetchChart_code, fetchChartUser, toggleWish, syncWishlist } from '../../../Slice/chartuserSlice'; 
import { addWishlistAsync, delWishlistAsync,fetchWishlistAsync } from '../../../Slice/wishlistSlice';
import StockItem from './StockItem';
import WishItem from './WishItem';


const StockList = ({filterName}) => {
    
    const dispatch = useDispatch();
    
    const stockData = useSelector((state) => state.chartuser.chartuserlist);
    
    let items = stockData?.list || [];
    if (filterName === "관심종목"){
        items = items.filter(stock => stock.is_wish === true);
    }else if (filterName === "카테고리"){
        items = [...items].sort(
            (a, b) => a.category_name.localeCompare(b.category_name, "ko")
        );
    }else if (filterName === "등락폭별"){
        items = [...items].sort(
            (a, b) => Math.abs(b.flu_range_percent) - Math.abs(a.flu_range_percent)
        );
    }
    
    const handleWishClick = (e, stock) => {
        e.stopPropagation(); 
        dispatch(toggleWish(stock.item_code));

        if (!stock.is_wish) { //아직 dispatch전이라 업뎃안됨
            dispatch(addWishlistAsync(stock.item_code));
        } else {
            dispatch(delWishlistAsync(stock.item_code));
        }
    };
    useEffect(() => { // useEffect는 async 가 불가해서 await 쓰기위해
                        // 함수 넣음
        const init = async () => {
            if (items.length === 0) {
                await dispatch(fetchChartUser());
            }
            const result = await dispatch(fetchWishlistAsync());
            const wishCodes = (result.payload || []).map(w => w.item_code);
            dispatch(syncWishlist(wishCodes));
        };
        init();
    }, [dispatch]);

    return (
        <div>
            <div className="border-b border-gray-100 px-4 py-3 text-sm font-semibold text-gray-700">
                종목 리스트 ({items.length})
            </div>
            <div className="divide-y divide-gray-100 max-h-[70vh] overflow-y-auto cursor-pointer">
                {items.map((item) => (<div key={item.item_code}>
                        <StockItem item={item} 
                            onClick={()=>dispatch(fetchChart_code(item.item_code))}
                            handleWishClick={(e)=>handleWishClick(e, item)}
                        />
                    </div>
                ))}
          </div>
        </div>
    );
};

export default StockList;