import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import App01 from './App01';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App01 /> 
    {/* 여기서 좌표 바꿔서 실행시켜야 한다. 그리고 실행은 브라우저에 localhost:3000 입력.*/}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
