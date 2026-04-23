import React from 'react';

// const ChartItem = () => {
//     return (
//         <div>
//             시작가격, 종료가격, 최고가, 최저가 이용해 1일 차트 출력
//             색깔도 구분
//         </div>
//     );
// };

// export default ChartItem;

const Candle = ({ item, showLabel, chart_height, priceToY }) => {
  const isUp = item.close >= item.open;

  const wickTop = priceToY(item.high);
  const wickBottom = priceToY(item.low);

  const bodyTop = priceToY(Math.max(item.open, item.close));
  const bodyBottom = priceToY(Math.min(item.open, item.close));
  const bodyHeight = Math.max(bodyBottom - bodyTop, 4);

  const candleColor = isUp ? "bg-blue-600" : "bg-red-500";
  const wickColor = isUp ? "bg-blue-700" : "bg-red-600";

  return (
    <div className="group relative flex flex-col items-center">
      {/* 툴팁 */}
      <div className="pointer-events-none absolute -top-4 z-30 hidden w-max rounded-md border border-gray-200 bg-white px-3 py-2 text-xs text-gray-700 shadow-lg group-hover:block">
        <div className="mb-1 font-semibold text-gray-800">{item.label}</div>
        <div>시가: {item.open.toLocaleString()}</div>
        <div>종가: {item.close.toLocaleString()}</div>
        <div>고가: {item.high.toLocaleString()}</div>
        <div>저가: {item.low.toLocaleString()}</div>
      </div>

      <div className="relative w-full" style={{ height: `${chart_height}px` }}>
        {/* 심지 */}
        <div
          className={`absolute left-1/2 w-[1px] -translate-x-1/2 ${wickColor}`}
          style={{
            top: `${wickTop}px`,
            height: `${Math.max(wickBottom - wickTop, 2)}px`,
          }}
        />

        {/* 몸통 */}
        <div
          className={`absolute left-1/2 w-3 -translate-x-1/2 ${candleColor}`}
          style={{
            top: `${bodyTop}px`,
            height: `${bodyHeight}px`,
          }}
        />
      </div>

      {/* 🔥 3칸마다 라벨 */}
      <div className="mt-1 h-4 text-[10px] text-gray-600">
        {showLabel ? item.label : ""}
      </div>
    </div>
  );
}

export default Candle;