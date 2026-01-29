// 1 . if 문
console.log("=== if 문 === ")

let a = 10;
if (a > 5){
    //if문의 조건이 true일 때 실행할 코드
    console.log(`${a}이(가) 5보다 커요`);
}

//코드가 한 줄 일 때는 scope 생략 가능
if (a > 3) console.log (`${a}이(가) 3보다 커요`);

// if - else
if (a > 20) {
    console.log(`${a}이(가) 20보다 커요`);
} else {
    // if 문의 모든 조건이 false 인 경우에도 무조건 실행시킬 코드
    console.log(`${a}이(가) 20보다 작거나 같아요.`);
}

// if - else if - else : 가독성 사유, if 중복 실행 등을 방지하기 위해 체인처럼 연결해 작성
let score = 85;

if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else if (score >= 70) {
    console.log("C");
} else if (score >= 60) {
    console.log("D");
}  else {
    console.log("F");
}

// // if문을 따로 따로 작성하는 경우
// if (score < 90 && score >= 80) {
//     console.log('B');
// }

// // 마지막 else 문도 else if문처럼 작성 가능
// else if (score < 60){
//     console.log('F');
// }

// //그러나 이렇게 될 경우에 코드를 쓰는 입장에서 글자를 많이 써야 하고
// // 실행될 때에도 조건에 만족하는지 불필요한 검사를 진행함.


// if문 중첩
console.log('=== if문 중첩 ===');

let userId = 'layla';
let userPw = '1234*';
let userInput = prompt('아이디를 입력하세요');

// if (userId === userInput) {
//     //아이디 맞음
//     let userInputPw = prompt('비밀번호를 입력하세요');
//     if (userPw === userInputPw) {
//         //비밀번호 같음
//         alert('로그인 성공');
//     } else {
//         alert('비밀번호가 일치하지 않습니다');
//     }
// } else {
//     alert('아이디가 일치하지 않습니다');
// }

// // 2 switch
// console.log('=== switch문 ===');

// let b = Number(prompt('숫자를 입력하세요'));

// switch (b) {
//     case 1:
//         //case는 b와 비교해 실행하고 case 첫 조건에 break; 없다면 무한히 실행됨
//         // 케이스 내 코드 작성시 무조건 break 사용해야 함.
//         console.log('b가 1이네요');
//         break;

//     case 2:
//     case 3:
//     case 4:
//         // case만 연달아 작성한 경우 해당 케이스 중 하나라도 만족하면 ":" 다음 코드 실행
//         console.log('b가 2 ~ 4중 하나네요');
//     case 5:
//         console.log('b가 5네요.');
//     default:
//         //위의 모든 조건들이 불만족할 때 무조건 실행되는 코드
//         // default로 실행할 코드가 없다면 작성하지 않아도 괜찮음
//         // default문은 꼭 작성하지 않아도 괜찮음 (생략 가능)
//         console.log('b는 어디에도 해당하지 않아요');
//         break;
// }


// 3. 삼항연산자
console.log('=== 삼항연산자 ===');
//간단한 조건문을 간결하게 표현하는데 사용

let num = 100;

//일반 if문
if (num > 50) {
    console.log('num이 50보다 커요');
} else {
    console.log('num이 50보다 작거나 같아요');
}

// 동일한 로직 삼항연산자로 변환
// 조건 ? 조건이 true 일 때 실행될 코드 : 조건이 false일 때 실행될 코드
num > 50 
    ? console.log('num이 50보다 커요') // ? 다음은 참일 때 실행
    : console.log('num이 50보다 작거나 같아요'); // : 다음은 거짓일 때 실행



console.log('=== 실습 1 ===');

let age = prompt('나이 입력하세요');

if (age >= 20) {
    console.log("성인");
} else if (age >= 17) {
    console.log("고등학생");
} else if (age >= 14) {
    console.log("중학생");
} else if (age >= 8) {
    console.log("초등학생");
}  else {
    console.log("유아");
}

console.log('=== 실습 2 ===');

let now = new Date().getHours(); //몇 시인지만 받아옴. JS 내장 메서드다.

now >  12
    ? console.log('오후') 
    : console.log('오전'); 

let time = new Date();

console.log(time);