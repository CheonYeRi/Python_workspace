// 1. var
// 더 이상 사용하지 않는 방법
// 프로젝트에서 이걸 쓰면 도망치세요.(리더님 말씀)

console.log('??', a); //선언되지 않은 변수 출력시 에러 발생x, 그냥 undefined 출력

// 변수 선언
var a;
console.log("변수 선언",a); //console log = print 와 비슷함.
// undefined 출력 (아직 a라는 변수에 값이 할당되지 않았기 때문)

//초기화, 값 할당

a = 10;
console.log('변수 초기화 값 할당',a);

//값 재할당

a = 500;
console.log('변수 값 재할당', a);

//변수 중복 선언
var a = 10000;
console.log('변수 중복 선언', a);


// ===========

// 2. let : 변수 재할당 가능, 중복 선언 불가

// 변수 선언

let b;
console.log('let 선언',b); //undefined 출력

// 변수 초기화

b =3.14;
console.log('let 초기화',b);

//변수 재할당

b = "재할당";
console.log('let 재할당',b); // 재할당 출력

//let b = '중복 선언 시도'; // let은 중복 선언이 불가능하고, 선언 시 에러 발생

// =====================

// 3. const: 변수 재할당 불가
// constant(상수)의 약자

// const 선언
// const c; //const를 사용한 변수 선언 시 초기화를 무조건 동시에 진행해야 함.

const c = 500000000;
console.log("const 선언 + 초기화", c);

//c = 'const 재할당 시도'; //const로 선언한 변수는 값 재할당 불가

// ======================

// 변수 네이밍 규칙 (팀프로젝트에서 네이밍 규칙은 통일하는 게 좋다)
// 여기서는 카멜과 파스칼을 자주 쓴다.

// 변수는 숫자로 시작할 수 없음.
// let 1var;

// 키워드 사용 불가
// let let;
// let for;
// let while;
// let if;

// 변수에 공백 사용 불가
//let my var;

// 사용 가능한 특수문자: _ , $
let my_var;
let $myVar;

//변수명 Tip
// 이름은 읽기 쉽도록
// 상수는 대문자로 선언해서 다른 개발자도 알 수 있게 만들기.