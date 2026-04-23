import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";

export const fetchUser = createAsyncThunk("user/fetchUser",async()=>{
  const res = await api.get("/users/me");
  return res.data;
})


const userSlice = createSlice({
  name: 'user',
  initialState: {
    login_id:null,
    user_nickname:null,
    money : 0,
    valuation : 0,
    created_at : null,
    refresh_token : null,
    isLoggedIn : false
  },
  reducers: {
    login: (state, action) => {
        state.isLoggedIn = true;
        const { login_id, user_nickname, money, valuation, created_at, refresh_token } = action.payload;
        state.login_id = login_id;
        state.user_nickname = user_nickname;
        state.money = money;
        state.valuation = valuation;
        state.created_at = created_at;
        state.token = refresh_token; 
    },
    logout: (state) => {
        state.isLoggedIn =false;
    },
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