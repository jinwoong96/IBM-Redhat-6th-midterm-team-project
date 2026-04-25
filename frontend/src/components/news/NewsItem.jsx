import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchNewsUser } from '../../Slice/newsuserSlice';

const NewsItem = () => {
    const dispatch = useDispatch();
    const newslist = useSelector((state)=>state.newsuser.newslist)

    useEffect(()=>{
        dispatch(fetchNewsUser());
    },[dispatch])
    return (
    <div>
        {newslist.length > 0 ? (
            newslist.map((news) => (
                <div key={news.news_id}>
                    <h4>{news.news_title}</h4>
                    <p>{news.news_comments}</p>
                </div>
            ))
        ) : (
            <p>뉴스가 없습니다.</p>
        )}
    </div>
);
};

export default NewsItem;