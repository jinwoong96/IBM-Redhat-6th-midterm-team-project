import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";

export const fetchChartUser = createAsyncThunk("chartuser/fetchChartUser", async () => {
    const res = await api.get("/chartuser/items");
    return res.data;
});


export const fetchChart_code = createAsyncThunk("chartuser/fetchChart_code", async (item_code) => {
    const res = await api.get(`/chartuser/items/${item_code}`);
    return res.data;
});

const chartuserSlice = createSlice({
    name: 'chartuser',
    initialState: {
        chartuserlist: [],      
        chartuserlist_code: [], 
    },
    reducers: {
        next_chart: (state, action) => {
            if (action.payload) {
                state.chartuserlist = action.payload;
            }
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchChartUser.fulfilled, (state, action) => {
                state.chartuserlist = action.payload;
            })
            .addCase(fetchChart_code.fulfilled, (state, action) => {
                state.chartuserlist_code = action.payload;
            });
    }
});

export const { next_chart } = chartuserSlice.actions;
export default chartuserSlice.reducer;