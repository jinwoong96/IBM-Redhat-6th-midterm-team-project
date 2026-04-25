import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";

export const fetchTrade = createAsyncThunk("trade/fetchTrade", async()=>{
    const res = await api.get("/trade");
    return res.data;
})
export const addTradeAsync = createAsyncThunk("trade/addTrade", async (tradeData) => {
    const res = await api.post("/trade", tradeData);
    return res.data;
});

const tradeSlice = createSlice({

    name : 'trade',
    initialState: {
        trades :[]
    },
    reducers:{},
    extraReducers: (builder) =>{
        builder
        .addCase(fetchTrade.fulfilled,(state,action)=>{
            state.trades = action.payload;
        })
        .addCase(addTradeAsync.fulfilled, (state, action) => {
                state.trades.unshift(action.payload);
        });
    }

})
export default tradeSlice.reducer;