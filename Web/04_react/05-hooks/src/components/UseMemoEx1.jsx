// useMemo
// 메모제이션으로 수행한 연산의 결과 값을 기억함으로써 불필요한 연산을 최소화

import { useMemo, useState } from "react";

function UseMemoEx() {
    const [count,setCount] = useState(0);
    const [input, setInput] = useState("");

    // //임의의 큰 연산을 하는 함수
    // const calc = () =>{
    //     console.log('열심히 계산 중...');
    //     for (let i = 0; 1 < 10000000000; i++){}

    //     return count ** 2;
    // }

    // [after]
    // count의 값이 바뀔 때만 함수를 실행
    // input 상태가 바뀌면 컴포넌트는 리랜더링 되지만, calc 연산되지 않도록
    const calcNum = useMemo(()=> {
        console.log('열심히 계산 중...');


        return count ** 2;
    }, [count]);

    return (
        <div>
            <div>테스트</div>
            <h1>useMemo Ex</h1>
            <input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
            <button onClick={()=> setCount(()=> count + 1)}>Plus</button>
            <p>count: {count} </p>
            {/* <p>calc: {calc()}</p> */}

            {/* after */}
            <p>calc: {calcNum}</p>
        </div>
    );
}

export default UseMemoEx;