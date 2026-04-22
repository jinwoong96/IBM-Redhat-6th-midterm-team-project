import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../api/api";
import axios from "axios";


const wishlistSlice = createSlice({
    name: 'wishlist',
    initialState: {
        wishlists: [] 
    },
    reducers: {
       
        add_wishlist: (state, action) => {
            const { wishlist_id, login_id, item_code } = action.payload;

            const new_wishlist = {
                wishlist_id,
                login_id,
                item_code
            };

            state.wishlists.push(new_wishlist);
        },
        del_wishlist: (state, action) => {
            const targetCode = action.payload; 

            state.wishlists = state.wishlists.filter(
                (item) => item.item_code !== targetCode
                );
        }
    },
});

export const { add_wishlist, del_wishlist } = wishlistSlice.actions;
export default wishlistSlice.reducer;