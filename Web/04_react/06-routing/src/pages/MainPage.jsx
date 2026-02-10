import { useSearchParams } from "react-router-dom";

function MainPage() {
    const [searchParams, setSearchParams] = useSearchParams();
    console.log(searchParams.get('mode')); //null or dark
    // http://localhost:3000/?mode=dark 식으로 뒤에 mode= dark하면 searchParams에서 dark가 찍힘 
    return (
        <div className={['main', searchParams.get('mode')].join(' ')}> 
        {/* .join(' ')식으로 공백 한 칸 넣어줘야 함. */}
            <h1>Home</h1>
            <button onClick={()=>{
                setSearchParams({mode: 'dark'});
            }}>Dark Mode</button>
        </div>
    );
}

export default MainPage;