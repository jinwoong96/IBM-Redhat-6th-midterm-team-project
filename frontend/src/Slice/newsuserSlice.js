import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";

export const fetchNewsUser = createAsyncThunk("newsuser/fetchNewsUser", async()=>{
    const res = await api.get("/newsuser");
    return res.data
})

export const fetchNews_init = createAsyncThunk("newsuser/fetchNews_init",async()=>{
    const res = await api.post("/newsuser/generate");
    return res.data
})

export const fetchNews_last = createAsyncThunk("newsuser/fetchNews_last", async()=>{
    const res = await api.get("/newsuser/latest")
    return res.data
})
const newsuserSlice = createSlice({
    name : 'newsuser',
    initialState :{
        newslist : [],
        today_news : null,
        last_news : null
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
        .addCase(fetchNews_init.fulfilled,(state,action)=>{
            state.today_news = action.payload;
        })
        .addCase(fetchNews_last.fulfilled,(state,action)=>{
            state.last_news = action.payload;
        })
    }


})


export default newsuserSlice.reducer;