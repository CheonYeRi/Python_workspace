import { useState } from "react";

function Fontcolor() {
    const [text,setText] = useState({text: "검은색 글자", color: "black"});

    return (
        <div>
            <div style={{ color: text.color, fontSize: "32px"}}>
                <b>{text.text}</b>
            </div>

            <button onClick={() => setText({text: "빨간색 글자", color: "red"})}>
                빨간색
            </button>
            <button onClick={() => setText({text: "파란색 글자", color: "blue"})}>
                파란색
            </button>            
        </div>
    );
}

export default Fontcolor ;