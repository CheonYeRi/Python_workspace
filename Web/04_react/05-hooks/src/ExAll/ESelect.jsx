function Select({setData}) {
    return (
        <>
            과일:
            <select onChange={(e)=> {
                setData((prev)=> {
                    return{...prev, fruit: e.target.value};
                });
            }}>
                <option value="apple">사과</option>
                <option value="banana">바나나</option>
                <option value="peach">복숭아</option>
                <option value="orange">오렌지</option>
                <option value="grape">포도</option>
            </select>
            배경색
            <select onChange={(e)=> {
                setData((prev)=> {
                    return{...prev, background: e.target.value};
                });
            }}>
                <option value="white">흰색</option>
                <option value="black">검정</option>
                <option value="yellow">노랑</option>
                <option value="lightblue">하늘색</option>
                <option value="pink">핑크</option>
            </select>
            글자색:
            <select
                onChange={(e) => {
                setData((prev) => ({
                    ...prev,
                    color: e.target.value,
                }));
                }}
            >
            <option value="black">검정</option>
            <option value="red">빨강</option>
            <option value="blue">파랑</option>
            <option value="green">초록</option>
            <option value="purple">보라</option>
            </select>
        </>
    );
}

export default Select;