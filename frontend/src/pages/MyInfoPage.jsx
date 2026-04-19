import React from 'react';
import MyInfo from '../components/myinfo/MyInfo';
import Assets from '../components/myinfo/Assets';
import Statistics from '../components/myinfo/Statistics';

const MyInfoPage = () => {
    return (
        <div>
            <MyInfo />
            <div className="grid grid-cols-2 gap-4">
                <section className="col-span-1">
                    <Assets />
                </section>
                <section className="col-span-1">
                    <Statistics />
                </section>
            </div>
        </div>
    );
};

export default MyInfoPage;