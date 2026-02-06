function Result(data) {
    const fruitE = {
        apple: "🍎",
        banana: "🍌",
        orange: "🍊",
        grape: "🍇",
        peach: "🍑",
    };

    return (
        <div 
            style={{backgroundColor: data.backgroundColor,
                color: data.color,
                padding: "20px",
                textAlign: "center",
                borderRadius: "8px",
            }}>
                <h3>과일: {data.fruitE}</h3>
                

        </div>
    );
}

export default Result;