import React from 'react';
import { Routes, Route } from 'react-router-dom'
import IntroPage from './pages/IntroPage';
// import RankingPage from './pages/RankingPage';
// import Home from './pages/Home';
// import LoginPage from './pages/LoginPage';
// import SignupPage from './pages/SignupPage';
// import InfoPage from './pages/InfoPage';
// import Provider from './context/Provider';
const App = () => {

  return (
    <Routes>
      <Route path="/" element={<IntroPage/>}/>
      {/* <Route path='/a' element={<Home/>}/> */}
      {/* <Route path="/b" element={<RankingPage/>}/> */}
      {/* <Route path='/c' element={<LoginPage/>}/> */}
      {/* <Route path='/d' element={<SignupPage/>}/> */}
      {/* <Route path="/e" element={<InfoPage/>}/> */}
    </Routes>
  );
};

export default App;