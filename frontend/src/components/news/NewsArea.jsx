import React, { useEffect } from 'react';
import NewsItem from './NewsItem';
import { useSelector, useDispatch } from 'react-redux';
import { fetchNewsUser } from '../../Slice/newsuserSlice'; 

const NewsArea = () => {

    const dispatch = useDispatch();
    const newslist = useSelector((state)=> state.newsuser.newslist)

    useEffect(()=>{
        dispatch(fetchNewsUser());
    },[dispatch])

    // newslist 가 현재 인증된 사용자의 뉴스 리스트
    return (
        <div>
            뉴스 영역 스타일링 해주기
            <NewsItem />
        </div>
    );
};

export default NewsArea;