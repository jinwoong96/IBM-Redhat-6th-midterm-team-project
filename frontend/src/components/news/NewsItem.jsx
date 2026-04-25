import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

const NewsItem = () => {
    const dispatch = useDispatch();
    return (
        <div>
            뉴스 제목, 내용 등 출력해주기
        </div>
    );
};

export default NewsItem;