import './App.css';
import Button from './Button';
import Counter from './Counter';
import Counter2 from './Counter2';
import FunctionComponent from './FunctionComponent';

function App() {
  return (
    <div className="App">
      <FunctionComponent name='로이' /> {/*셀프 클로징 */} 
      <FunctionComponent /> 
      {/* 화면 상에서 name 변수가 나오지 않고 undefined 나옴 
      export default function FunctionComponent({ name = '기본 이름' }) 하면
      안 나올 때 기본 값으로 '기본 이름'이 대체되어 나옴*/}

      <hr />
      <Button link="https://www.google.com">Google</Button>
      
      <hr />
      <h2>useState활용</h2>
      <Counter />

      <hr />
      <h2>useState실습</h2>
      <Counter2 />

    </div>
  );
}

export default App;
