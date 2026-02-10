import { useNavigate, useParams, useSearchParams } from "react-router-dom";

function SearchParams() {
    const { name } = useParams();
    
    const [searchParams] = useSearchParams();
    const keyWord = searchParams.get("name");
    const navigate = useNavigate();
    return (
        <div>
            
            <button onClick={()=> navigate(-1)}>뒤로 가기</button>
            {keyWord && (
                <h3>진짜 이름은 <span style={{color:'green'}}>{ keyWord }</span>입니다. </h3>)}
        </div>
    );
}

export default SearchParams;