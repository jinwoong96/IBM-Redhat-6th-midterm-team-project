import React from 'react';
import ChartList from './ChartList';
import Candle from './Candle';

// const ChartArea = () => {
//     return (
//         <div>
//             <div>차트</div>
//             <ChartList />
//         </div>
//     );
// };

// export default ChartArea;


const candleData = [
  { label: "-3/1", open: 50000, close: 50500, high: 52000, low: 49800 },
  { label: "-3/2", open: 50500, close: 53000, high: 57200, low: 50200 },
  { label: "-3/3", open: 52000, close: 45000, high: 52000, low: 44800 },
  { label: "-2/1", open: 52000, close: 55500, high: 55500, low: 52000 },
  { label: "-2/2", open: 52000, close: 52500, high: 52500, low: 52000 },
  { label: "-2/3", open: 53000, close: 54800, high: 54800, low: 53000 },
  { label: "-1/1", open: 52000, close: 56500, high: 58500, low: 52000 },
  { label: "-1/2", open: 55000, close: 49000, high: 55200, low: 49000 },
  { label: "-1/3", open: 52000, close: 54500, high: 54500, low: 52000 },
  { label: "1/1", open: 52000, close: 45000, high: 52000, low: 44800 },
];

// 이것들은 현재 차트 데이터 목록 이용해서 계산(chart height는 원하는 높이에 따라 고정값 사용)
const MIN_PRICE = 44000;
const MAX_PRICE = 59000;
const CHART_HEIGHT = 180;
const priceTicks = [57000, 53000, 49000, 45000];

function priceToY(price) {
  return ((MAX_PRICE - price) / (MAX_PRICE - MIN_PRICE)) * CHART_HEIGHT;
}



function ChartArea() {
  const visibleData = candleData.slice(-30);
  const emptyCount = 30 - visibleData.length;

  // 현재 선택된 종목 이름, 종목 코드, 차트 데이터 리스트 불러옴

  return (
    <div className="inline-block border border-gray-300 bg-[#efefef]">
      <div className="border-b border-gray-300 bg-[#e5e5e5] px-3 py-1 text-sm font-medium text-gray-700">
        GS(78930) 현재가: 53,000
      </div>

      <div className="flex gap-3 p-3">
        {/* Y축 */}
        <div className="relative w-14 shrink-0" style={{ height: `${CHART_HEIGHT}px` }}>
          {priceTicks.map((price) => (
            <div
              key={price}
              className="absolute right-0 translate-y-1/2 text-sm text-gray-600"
              style={{ top: `${priceToY(price)}px` }}
            >
              {price.toLocaleString()}
            </div>
          ))}
        </div>

        {/* 차트 영역 */}
        <div className="relative min-w-175 flex-1">
          {/* 가로선 */}
          <div
            className="absolute left-0 top-0 z-0 w-full"
            style={{ height: `${CHART_HEIGHT}px` }}
          >
            {priceTicks.map((price) => (
              <div
                key={price}
                className="absolute left-0 w-full border-t border-sky-200"
                style={{ top: `${priceToY(price)}px` }}
              />
            ))}
          </div>

          {/* 30칸 고정 grid */}
          <div className="relative z-10 grid grid-cols-30 gap-1">
            {/* 🔥 왼쪽 빈칸 */}
            {Array.from({ length: emptyCount }).map((_, i) => (
              <div key={`empty-${i}`} />
            ))}

            {/* 🔥 실제 데이터 */}
            {visibleData.map((item, index) => {
              const showLabel = (index + 1) % 3 === 0;

              return (
                <Candle
                  key={item.label}
                  item={item}
                  showLabel={showLabel}
                  priceToY={priceToY}
                />
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default ChartArea;