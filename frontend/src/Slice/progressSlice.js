import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";


export const fetchProgress = createAsyncThunk("progress/fetchProgress",async()=>{
    const res = await api.put("/progress/next_turn");
    return res.data;
})

const progressSlice = createSlice({
    name : "progress",
    initialState:{
        next_data: []
    },
    reducers:{},
    extraReducers:(builder)=>{
        builder
        .addCase(fetchProgress.fulfilled,(state,action)=>{
            state.next_data = action.payload;
        })
    }



})


export default progressSlice.reducer;