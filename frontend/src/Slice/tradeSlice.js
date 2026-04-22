import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";

export const fetchTrade = createAsyncThunk("trade/fetchTrade", async(limit,offset)=>{
    const res = await api.get("/trade");
    return res.data;
})


const tradeSlice = createSlice({

    name : 'trade',
    initialState: {
        trades :[]
    },
    reducers:{
        add_trade :(state,action) =>{
            const {trade_id,buy_type,price,quantity,trade_day,login_id,item_code}=action.payload;
            const new_trade = {
                trade_id,
                buy_type,
                price,
                quantity,
                trade_day,
                login_id,
                item_code
            };
            state.trades.push(new_trade);
        }
    },
    extraReducers: (builder) =>{
        builder
        .addCase(fetchTrade.fulfilled,(state,action)=>{
            state.trades = action.payload;
        })
    }

})

export const {add_trade} = tradeSlice.actions;
export default tradeSlice.reducer;