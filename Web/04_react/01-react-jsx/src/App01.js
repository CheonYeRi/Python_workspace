
// function App() {
//     const name = "로이"
//     const animal = "강아지"
//     return (
//         <> 
//         <div className="App">
//         <h2>실습 1 제 반려 동물의 이름은 {name}입니다.</h2>
//         <h2>{name}은 {animal}입니다.</h2>

//         <div> 실습 2 {3 + 5 === 8 ? "정답입니다." : "틀렸습니다."}</div>
//         </div>
//         </> // 빈 플래그먼트만 사용해 감싸기 가능하다.
//     );
// }

function App(){
    const a = 5;
    const b = 3;
    return(
        <div>
            { a > b && <p>{a}가 {b}보다 큽니다.</p>}
        </div>
    );
}    


export default App;