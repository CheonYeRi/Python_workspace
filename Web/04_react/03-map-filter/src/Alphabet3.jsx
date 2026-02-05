import { useState } from "react";

function Alphabet3() {
    /*
        {
            id: 1, alpha: 'a',
        }
    */
    const [alphabet, setAlphabet] = useState([]);
    //input 값을 state변수로 선언
    const [inputValue, setInputValue] = useState("");

    const addAlpha = () => {
        const newAlpha = alphabet.concat({
            id: alphabet.length + 1,
            alpha: inputValue,
        })
        setAlphabet(newAlpha);
        setInputValue("");
    };
    const deleteAlpha = (targetId) => {
        const newAlpha = alphabet.filter((alpha)=> alpha.id !== targetId);
        setAlphabet(newAlpha);
    }


    return ( 
        <>
            <input type="text" placeholder="알파벳 입력" value={inputValue} 
            onChange={(e)=> setInputValue(e.target.value)} />
            <button onClick={addAlpha}>ADD </button>
            {/* value는 const 선언한 input변수들 넣고, onChange 마찬가지다 npm start해야 실행 */}
            {/* 더블 클릭으로 삭제 이벤트 추가 */}
            <ol>
                {alphabet.map((value) => {
                    return <li key={value.id} onDoubleClick={() => deleteAlpha(value.id)}> {value.alpha}</li>;
                    // () = > 함수() : 실행될 때 호출한다 구조.
                })}
            </ol>

            {/* 단축 평가 */}
            {alphabet.length === 0 && <span>알파벳을 입력해주세요!</span>}
        </>
    );
}

export default Alphabet3;