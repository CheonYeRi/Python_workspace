import { useState } from "react";

function Alphabet2() {
    const [alphabet, setAlphabet] = useState(['a','b','c','d','e']);
    //input 값을 state변수로 선언

    const [inputValue, setInputValue] = useState("");

    const addAlpha = () => {
        const newAlpha = [...alphabet, inputValue]; 
        setAlphabet(newAlpha);
        setInputValue("");
    };


    return ( 
        <>
            <input type="text" placeholder="알파벳 입력" value={inputValue} 
            onChange={(e)=> setInputValue(e.target.value)} />
            <button onClick={addAlpha}>ADD </button>
            <ol>
                {alphabet.map((value,idx) => {
                    return <li key={idx}>{value}</li>;
                })}
            </ol>
        </>
    );
}

export default Alphabet2;