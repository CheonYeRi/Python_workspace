function Result({data}) {
    const fruitE = {
        apple: "🍎",
        banana: "🍌",
        orange: "🍊",
        grape: "🍇",
        peach: "🍑",
    };
    const{fruit, background,color,content} = data;

    return (
        <div 
            style={{backgroundColor: data.backgroundColor,
                color: data.color,
                padding: "20px",
                textAlign: "center",
                borderRadius: "8px",
            }}>
        <h3>과일: {fruit}</h3>
        <h3>배경색: {background}</h3>
        <h3>글자색: {color}</h3>
        <p>내용: {content}</p>

            <div style={{ fontSize: "50px", marginTop: "10px" }}>
            {fruitE[fruit]}</div>
        </div>
    );
}

export default Result;