
import { Route, Routes } from 'react-router-dom';
import Header from './component/Header';
import './styles/App.css';
import MainPage from './pages/MainPage';
import ProductPage from './pages/ProductPage';
import ProductDetailPage from './pages/ProductDetailPage';
import { useEffect, useState } from 'react';
import axios from 'axios';

import Navbar from './Router/Navbar';
import Student from './Router/kdt';
import CodingOn from './Router/codingon';
import SearchParams from './Router/searchparams';

function App() {
  // const [products, setProducts] = useState([]);

  // const getProducts = async () => {
  //   const res = await axios.get('https://jsonplaceholder.typicode.com/comments');
  //   console.log(res.data);
  //   setProducts(res.data.slice(0, 10));
  // };

  // useEffect(()=> {
  //   getProducts();
  // }, []); //[] 추가하지 않으면 무한으로 리렌더링 함. 
  return (
    <div className="App">
      {/* <Header /> */}
      <Navbar />
      <Routes>
        {/* <Route path='/' element={< MainPage />} />
        <Route path='/products' element={<ProductPage products={products} />} />
        <Route path='/products/:productId' element={<ProductDetailPage products={products} />} /> */}
        <Route path="/student/kdt" element={<Student />} />
        <Route path="/student/codingon" element={<CodingOn />} />
        <Route path="/student/:name" element={<SearchParams />} />
      </Routes>
    </div>
  );
}

export default App;
