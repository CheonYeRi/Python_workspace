// 1. 함수 선언

// 함수 호이스팅(Hoisting)
// 컴파일 확인 후 실행 과정 중, 컴파일 진행 때 작성된 함수를 미리 저장한다.
// 함수 표현식, 화살표 함수는 변수 선언과 같은 양식으로 쓰고, 변수는 선언해야 작동되므로
// 변수 처리 기준과 똑같이 호출 X 인 것.

// 함수 선언식으로 함수를 만들었을 때는 선언보다 위에서 호출 가능
// 함수 표현식, 화살표 함수는 호출 불가.
console.log('(함수 선언식, 선언보다 위에서 호출)', myFunc('어라라'));

// console.log('(화살표 함수, 선언보다 위에서 호출)', square(10,8)); // 이건 안됨.

// 1-1 함수 선언신(기본적인 함수 선언 방법)
function myFunc(str) {
    //중괄호 내부에 함수 호출 시 동작할 코드 작성
    return str;
}

myFunc("이리 작성해도 console 창에 안 뜬다.") // console.log() 안 했으니까. 작성 O 출력 X 
console.log(myFunc("이 양식으로 써야 console창에 뜬다."));

//간단 실습
// 함수를 호출만 해도 콘솔에 찍히게 하기
function myFunc2(str) {
    console.log(str);
}

myFunc2("이렇게 호출만 해도 콘솔에 찍혀야 해요!");

// 1-2 함수 표현식
// 변수에 익명함수를 할당하는 방법
const myFunc3 = function(){
    console.log('이렇게 함수 표현식으로 함수를 선언할 수 있어요.');
};

myFunc3(); //이렇게 불러도 찍힘.

// 1-3. 화살표 함수 () => {}
// 콜백함수 (어떤 코드나 로직 안에 작성할 때 많이 사용)
const arrowFunc = () => {
    // 화살표 함수는 {} 안에 꼭 return이 되어야 함.
    return '이렇게 화살표 함수를 사용할 수 있다.'
};

// 한 줄로 작성 + 괄호 없는 경우에는 해당 내용을 자동으로 return
// 명시적으로 return을 하자고 약속했기에 꼭 쓰라고 한다.
const arrowFunc2 = () => '이렇게 쓸 수도 있어요.';
arrowFunc2

console.log('-- 여기 보세요 --');
console.log(arrowFunc2); // 호출 안하고 변수에 찍힌 버전 == () => '이렇게 쓸 수도 있어요' 출력
console.log(arrowFunc2()); // () 사용해서 함수를 호출한 버전 == 이렇게 쓸 수도 있어요 출력


// 사각형의 넓이를 구하는 화살표 함수
const square = (w, h) => w * h;

console.log('사각형의 넓이 구하기', square(10,8)); //80, 작동됨

function noReturnFunc(width,height) {
    width * height;
}

console.log(noReturnFunc(5, 7)); 
// return 하지 않으면 함수 스코프 내부 코드 실행되고 출력 X. undefined 됨.


console.log('함수 실습 1');

function multifly(x,y) {
    return x * y
};

console.log(multifly(3,7));
console.log(multifly(2,2));


console.log('함수 실습 2');

const Square = function(x){
    console.log(x ** 2);
}

Square(4);
Square(11);
Square(5);