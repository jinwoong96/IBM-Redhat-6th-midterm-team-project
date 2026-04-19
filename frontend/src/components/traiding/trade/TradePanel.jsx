import React from 'react';

const TradePanel = () => {
    // state 관리(가격, 수량, 종목명 등)

    return (
        <div>
            <div>거래</div>
            <div>수량</div>
            <input type="number" />
            <div>수량</div>
            <div>1주 가격</div>
            <div>총 금액</div>
            <div>
                <button onClick={()=>{alert("매수 누르면 실행할 함수")}}>매수</button>
                <button onClick={()=>{alert("매도 누르면 실행할 함수")}}>매도</button>
            </div>
        </div>
    );
};

export default TradePanel;