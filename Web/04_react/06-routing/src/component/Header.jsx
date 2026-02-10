import { Link } from "react-router-dom";


function Header() {
    
    return (
        <header>
            <span> Router Tutorial</span>
            <ul>
                <li><Link to='/'>Home</Link></li>
                <li><Link to ='/products'>Products</Link></li> 
                {/* Link를 통해 App.js에 설정한 Route path= 값을 지정하면 그쪽으로 전환되게 해줌. */}
            </ul>
        </header>
    );
}

export default Header;