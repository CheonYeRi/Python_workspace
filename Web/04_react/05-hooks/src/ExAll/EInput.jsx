
function Input(setData) {

    const handleChange = (e) => {
        const value = e.target.value(); //입력 값 가져온다.
        setData((prev) => ({
            ...prev,
            content: value,
        }));
    }
    return (
        <div>
            <input type="text" placeholder="내용" onChange={handleChange}/>
        </div>
    );
}

export default Input;