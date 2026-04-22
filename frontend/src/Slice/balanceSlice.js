import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";

export const fetchMyBalance  = createAsyncThunk("balance/fetchMyBalance", async () =>{
    const res = await api.get("/balance");
    return res.data;
})


const balanceSlice = createSlice ({
    name : 'balance',
    initialState:{
        my_balance : []
    },
    reducers:{},
    extraReducers:(builder)=>{
        builder
        .addCase(fetchMyBalance.fulfilled, (state,action)=>{
            const {login_id,item_code,quantity,purchase_price,val_price,val_profit_and_loss,rate_of_return}= action.payload;
            state.login_id=login_id;
            state.item_code=item_code;
            state.quantity=quantity;
            state.purchase_price=purchase_price;
            state.val_price=val_price;
            state.val_profit_and_loss=val_profit_and_loss;
            state.rate_of_return=rate_of_return;            

        })
    }
})

export default balanceSlice.reducer;