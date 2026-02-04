export default function Food({ food = '기본 값' }){
    return (
        <div> 
            <div>
                <span style={{color : 'red'}}> {food} </span>
                는 라구 소스의 일종으로, 볼로냐 지방에서 유래한 고전적인 미트 소스 파스타이다.
            </div>
        </div>
    );
}
