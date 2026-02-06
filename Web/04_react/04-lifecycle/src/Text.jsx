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

// 실습 답안
// import { useState } from "react";

// function Fontcolor() {
//     const [text,setText] = useState({text: "검은색 글자", color: "black"});

//     const handleColor = (color, text) => {
//         setText({color,text});
//     };

//     return (
//         <div>
//             <h4 style={{color: text.color}}>{text.text}</h4>

//             <button onClick={(e) => handleColor('red',e.target.innerText)}>
//                 빨간색
//             </button>
//             <button onClick={(e) => handleColor('red',e.target.innerText)}>
//                 파란색
//             </button>            
//         </div>
//     );
// }

// export default Fontcolor ;