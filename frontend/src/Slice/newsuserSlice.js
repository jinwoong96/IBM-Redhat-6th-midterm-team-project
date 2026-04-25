import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";

export const fetchNewsUser = createAsyncThunk("newsuser/fetchNewsUser", async()=>{
    const res = await api.get("/newsuser");
    return res.data
})

const newsuserSlice = createSlice({
    name : 'newsuser',
    initialState :{
        newslist : []
    },
    reducers:{
        add_news : (state,action) =>{
            const {news_user_id,day,login_id,news_id} = action.payload;
            const new_news = {
                news_user_id,
                day,
                login_id,
                news_id
            };
            state.newslist.push(new_news);
        }
    },
    extraReducers:(builder)=>{
        builder
        .addCase(fetchNewsUser.fulfilled, (state,action)=>{
            state.newslist = action.payload;

        })
    }


})


export default newsuserSlice.reducer;