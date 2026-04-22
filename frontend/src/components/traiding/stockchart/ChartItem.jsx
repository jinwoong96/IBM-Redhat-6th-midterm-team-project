import React from 'react';
import { useSelector } from 'react-redux';

const ChartItem = () => { // 종목리스트에서 종목 누르면 dispatch로 item 코드를 넘겨줘야됨
    const chartData = useSelector((state) => state.chartuser.chartuserlist_code);


    const currentItemCode = chartData[chartData.length - 1]?.item_code;

    return (
        <div style={{ padding: '15px', border: '1px solid #ccc' }}>
            <h3>{currentItemCode} 상세 차트 (최근 20일)</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {chartData.map((day, index) => {
       
                    const isUp = day.end_price >= day.start_price;
                    const color = isUp ? '#f03e3e' : '#1971c2'; 

                    return (
                        <div key={day.chart_user_id || index} style={{
                            display: 'grid',
                            gridTemplateColumns: '80px 1fr 1fr 1fr 1fr',
                            padding: '8px',
                            border: `1px solid ${color}`,
                            backgroundColor: isUp ? '#fff5f5' : '#f0f4f8',
                            borderRadius: '4px',
                            fontSize: '0.85rem'
                        }}>
                            <span style={{ fontWeight: 'bold' }}>Day {day.day}</span>
                            <span>시: {day.start_price.toLocaleString()}</span>
                            <span style={{ color: color, fontWeight: 'bold' }}>
                                종: {day.end_price.toLocaleString()}
                            </span>
                            <span>고: {day.max_price.toLocaleString()}</span>
                            <span>저: {day.min_price.toLocaleString()}</span>
                        </div>
                    );
                })}
            </div>
        </div>
    );
};