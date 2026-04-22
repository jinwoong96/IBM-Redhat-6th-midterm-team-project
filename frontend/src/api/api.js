import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', 
  timeout: 5000, // 5초 넘으면 에러 처리
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;