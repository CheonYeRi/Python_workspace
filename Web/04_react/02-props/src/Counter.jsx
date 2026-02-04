import { useState } from "react";

function Counter() {
    const [number, setNumber] = useState(0);
    let num = 0;
    
    const handlePlus = () => setNumber(number + 1);
    return (  
        <div>
            <h1>{number}</h1>
            <button onClick={handlePlus}>Plus 1</button> 
            {/* onClick에 변수 지정한 setNumber를 갖고와서 적용함*/}

            <h1>{num}</h1>
            <button onClick={()=> {
                num = num + 1;
                console.log ('num', num);
                }}> Plus 1</button>
                {/* 변수로 선언한 값은 리랜더링 되어도 화면에 반영되지 않는다. */}
                {/* 기존의 html에서 함수 이름을 문자열에 () 붙이고 했지만 
                리액트에서 적용하면 무한히 반복 실행하는 걸로 적용되니 이름만 등록해야 함.*/}
        </div>
    );
}

export default Counter;