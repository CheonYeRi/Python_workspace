import logo from './logo.svg';
import './App.css';

function App() {
  const name = 'Luna';
  const styles = {
    backgroundColor: 'yellow',
    color: 'pink',
    fontSize: '48px',
  };
  return ( // return 은 화면에 보여지는 양식을 작성한다 보면 됨
    <> 
      <div className="App">
      {/* JSX 문법 */}
      {/* 1. 하나로 감싸인 요소 */}
      <div>반가워요</div>
      {/* 2. javascript 표현식 사용 
        - {}로 감싸면 js 표현식 사용 가능
        - {} 안에 삼항 연산자 사용 가능(if, for문 불가능)
      */}
      <div>{name} 안녕하세요.</div>
      <div>{name === "Luna" ? "반갑습니다" : "누구세요?"}</div>

      {/* 
      3. style 속성
      - 리액트에서 dom 요소에 스타일 적용시 문자열 x -> 객체 사용
      - 스타일 이름 중 하이픈(-) 포함시 camelCase로 적용
       */}
        <div style={styles}>하이</div>
        <div style={{
          backgroundColor: 'yellow',
          color: "pink",
          fontSize: '48px',
        }}>반가워요
        </div>

        {/* 
        4. className 사용
        - class 속성이 아닌 className 속성 사용!
        
        5. 종료 태그가 없는 태그의 사용
        - 기존의 종료 태그가 없는 태그를 사용하더라도 종료 태그를 작성해야 함 or self-closing

        6. 주석
          -// :jsx 외부 주석 
         */}
      </div>
    </> // 빈 플래그먼트만 사용해 감싸기 가능하다.
  );
}

export default App;
