import PropTypes from "prop-types";

// interface Props {
//     name?: Srting,
//     age: Number
// } 타임 스크립트 사용하는 건데 여기까지 알 필요 없다고 한다...

export default function FunctionComponent({ name = '기본 이름' }){
    const student = '홍길동';
    // console.log(props.name);
    // const { name } = props;
    return (
        <div> 
            <h1>안녕! {student}</h1>
            {/* <div>넘겨받은 props {props.name}</div> */}
            <div>const 이름으로 선언, 넘겨받은 {name}</div>
        </div>
    );
}

// 리액트 18 version 가능 -> typeScript 
FunctionComponent.protoTypes = {
    age: PropTypes.number,
}