import { configureStore } from '@reduxjs/toolkit'
import userReducer from '../Slice/userSlice'
import rankingReducer from '../Slice/rankingSlice'
import balanceReducer from '../Slice/balanceSlice'
import wishlistReducer from '../Slice/wishlistSlice'
import chartuserReducer from '../Slice/chartuserSlice'
export const store = configureStore({
    reducer : {
        user : userReducer,
        rank : rankingReducer,
        wishlist : wishlistReducer,
        // trade : tradeReducer,
        // progress : progressReducer,
        // newsuser : newsuserReducer,
        chartuser : chartuserReducer,
        balance : balanceReducer
    }
})