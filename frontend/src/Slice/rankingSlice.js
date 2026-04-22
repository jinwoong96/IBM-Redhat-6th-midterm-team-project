import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";
// 1. 내 랭킹 정보 조회 (ID 이용)
// export const fetchMyRanking = createAsyncThunk("rank/fetchMyRanking", async () => {
//   const res = await api.get("/ranking/me");
//   return res.data;
// });

// 2. 상위 10명 조회 (내림차순)
export const fetchTopRankings = createAsyncThunk("rank/fetchTopRankings", async () => {
  const res = await api.get("/ranking");
  return res.data;
});
const rankingSlice = createSlice({
    name: 'rank',
    initialState:{
        myRanking : {
        ranking_id:0,
        max_accounts:0,
        max_plus:0.0,
        day:0,
        login_id:null,
        },
        topRankings:[]
    },
    reducers:{},
    extraReducers:(builder) =>{
        builder
        // .addCase(fetchMyRanking.fulfilled, (state,action)=>{
        //     const {ranking_id,max_accounts,max_plus,day,login_id} = action.payload;
        //     state.myRanking.ranking_id = ranking_id;
        //     state.myRanking.max_accounts = max_accounts;
        //     state.myRanking.max_plus = max_plus;
        //     state.myRanking.day = day;
        //     state.myRanking.login_id = login_id;
        // })
        .addCase(fetchTopRankings.fulfilled, (state,action)=>{
            state.topRankings =action.payload;
        })
    }


})

export default rankingSlice.reducer;