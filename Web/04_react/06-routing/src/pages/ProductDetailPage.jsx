import { useNavigate, useParams } from "react-router-dom";
// import { productInfos } from "../component/ProductList";

function ProductDetailPage({products}) {
    const {productId} = useParams(); //string 타입으로 반환 ex) '2'
    const product = products[Number(productId) - 1];
    //Number로 변환한 후 -1 적용해 인덱스 값으로 지정함 (id값은 1부터이나 인덱스는 0부터여서)
    //export된 변수를 갖고와서 import해서 적용

    //navigate
    const navigate = useNavigate();
    return (
        <div>
            <h1>Product Detail Page</h1>
            <button onClick={()=> navigate(-1)}>뒤로가기</button>
            <button onClick={()=> navigate('/')}>홈으로 이동하기</button>
            {products.length !==0 ? (
                <ul>
                    <li>상품 번호 : {product.id}</li>
                    <li>상품명: {product.name}</li>
                    <li>판매자: {product.email}</li>
                    <li>상세 설명: {product.body}</li>
                </ul>
            ) :(
                <div> Loading </div>
            )}
            {/* 직접 경로접속시 막히면 접근 안되는 걸 디버깅함. */}
        </div>
    );
}

export default ProductDetailPage;