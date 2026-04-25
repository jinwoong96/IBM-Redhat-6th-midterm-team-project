import React from 'react';
import { useSelector } from 'react-redux';

const ChartItem = () => {
    const chartDataObj = useSelector((state) => state.chartuser.chartuserlist_code);

    const chartData = chartDataObj?.list || []; //리스트만 빼겠다
    const itemName = chartDataObj?.item_name || "종목명"; // 종목 이름을 빼겠다. 이름없으면 기본값 
    const itemCode = chartData[0]?.item_code || ""; // 그냥 다 item 코드 같으니 0번째에서 item_code뺌

    if (chartData.length === 0) {
        return <div>종목을 클릭하여 차트를 불러오세요.</div>;
    }

    return (
        <div>
            <h3>{itemName} ({itemCode}) 상세 차트 (최근 20일)</h3>
            
            <div>
                {chartData.map((day, index) => {
                    const isUp = day.end_price >= day.start_price;
                    const statusColor = isUp ? 'red' : 'blue';

                    return (
                        <div key={day.chart_user_id || index} style={{ borderBottom: '1px solid #eee' }}>
                            <span>[Day {day.day}] </span>
                            <span>시가: {day.start_price.toLocaleString()} | </span>
                            <span style={{ color: statusColor, fontWeight: 'bold' }}>
                                종가: {day.end_price.toLocaleString()} 
                            </span>
                            <span> | 고가: {day.max_price.toLocaleString()}</span>
                            <span> | 저가: {day.min_price.toLocaleString()}</span>
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default ChartItem;