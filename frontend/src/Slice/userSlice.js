import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";

export const fetchUser = createAsyncThunk("user/fetchUser",async()=>{
  const res = await api.get("/users/me");
  return res.data;
})


const userSlice = createSlice({
    // 로그인 성공 시 그 유저의 데이터 
  name: 'user',
  initialState: {
    login_id:null,
    user_nickname:null,
    user_password:null,
    money : 0,
    valuation : 0,
    created_at : null,
    refresh_token : null,
    isLoggedIn : false
  },
  reducers: {
    // 1.  로그인 성공 시 성공한 상태 저장
    // 2.  user/me 로 내정보 다 가져와서 상태 업데이트 
    login: (state, action) => {
        state.isLoggedIn = true;
        const {login_id,user_nickname,money,valuation,created_at,refresh_token}= action.payload;
        state.login_id = login_id;
        state.user_nickname = user_nickname;
        state.money = money;
        state.valuation = valuation;
        state.created_at = created_at;
        state.refresh_token = refresh_token;      
        
    },
    logout: (state) => {
        state.isLoggedIn =false;
        // state 전부 초기화
    },
    // 닉네임 , 패스워드 받아서 지금 유저 업데이트
    update: (state,action) =>{
        const {user_nickname,user_password}= action.payload;
        state.user_nickname = user_nickname;
        state.user_password = user_password;
    }
  },
  extraReducers: (builder) => {
    builder
    .addCase(fetchUser.fulfilled, (state,action)=>{
      const {login_id,user_nickname,user_password,money,valuation,created_at,refresh_token}=action.payload;
      state.login_id =login_id;
      state.user_nickname=user_nickname;
      state.user_password=user_password;
      state.money=money;
      state.valuation=valuation;
      state.created_at=created_at;
      state.refresh_token=refresh_token;
    })
  }
});

export const { login, logout, update } = userSlice.actions;
export default userSlice.reducer;