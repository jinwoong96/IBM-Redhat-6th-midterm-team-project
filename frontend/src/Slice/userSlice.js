import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";

export const fetchUser = createAsyncThunk("user/fetchUser",async()=>{
  const res = await api.get("/users/me");
  return res.data;
})

export const updateUser = createAsyncThunk("user/updateUser", async (updateData) => {
    const res = await api.put("/users", updateData);
    return res.data; 
});

export const logout = createAsyncThunk("user/logout", async (_, thunkAPI) => {
      const res = await api.post("/users/logout"); 
      return res.data;
  
});
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
    .addCase(updateUser.fulfilled,(state,action)=>{
      Object.assign(state, action.payload);
    })
    .addCase(logout.fulfilled, (state)=>{
        state.login_id = null;
        state.user_nickname = null;
        state.money = 0;
        state.valuation = 0;
        state.created_at = null;
        state.refresh_token = null;
        state.isLoggedIn = false;   
    })
  }
});

// 중복 확인 Thunk
export const checkDuplicate = createAsyncThunk(
    "user/checkDuplicate",
    async ({ login_id, nickname }, { rejectWithValue }) => {
        try {
            const params = login_id ? { login_id } : { nickname };
            const res = await api.get("/users/check-duplicate", { params });
            return res.data; // True 반환
        } catch (err) {
            return rejectWithValue(err.response.data.detail);
        }
    }
);

const userSlice = createSlice({
    name: 'user',
    initialState: {
        // ... 기존 상태 ...
        dupCheck: { id: false, nickname: false }, // 중복 확인 완료 여부
        error: null
    },
    extraReducers: (builder) => {
        builder
            // ... 기존 케이스 ...
            .addCase(checkDuplicate.fulfilled, (state, action) => {
                state.error = null;
            })
            .addCase(checkDuplicate.rejected, (state, action) => {
                state.error = action.payload;
            });
    }
});
export const { login} = userSlice.actions;
export default userSlice.reducer;