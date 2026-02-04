import { useState } from "react";

function Counter2() {
    const [number, setNumber] = useState(0);
    
    const increase = () => setNumber(number + 1);
    const decrease = () => setNumber(number - 2);
    return (  
        <div>
            <h1>{number}</h1>
            <button onClick={increase}>Plus</button>
            <button onClick={decrease}>Minus</button>
        </div>
    );
}

export default Counter2;