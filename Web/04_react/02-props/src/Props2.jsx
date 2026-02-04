
const Book = (props) => {
    const { title, author,price,type } = props;
    return (
        <>
            <h1 style={{color: 'orange'}}> 이번주 추천 서적 </h1>
            <img src="https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791188331796.jpg" alt="돈의 속성" width="500"/>
            <h1 className="title"> {title} </h1>
            <div className="content">저자: {author}</div>
            <div className="content">판매가: {price}</div>
            <div className="content">구분: {type}</div>
        </>
    )
}

export default Book