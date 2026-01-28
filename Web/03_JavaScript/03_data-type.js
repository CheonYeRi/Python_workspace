// 원시 자료형

// 1. 문자열(string)
const str = "좋은 아침";
console.log(str);

// 문자열 연산
const str2 = "오늘도 화이팅😊"; //window + . 누르면 이모지가 나온다.
console.log(str + str2);

const name = "Layla";
const age = 20;
console.log("안녕하세요 저는" + name + "이고, 나이는" + age +"살 입니다.😊");
// 안녕하세요, 저는 Layla이고 나이는 20살 입니다.😊

//탬플릿 리터럴
//변수와 문자열을 함께 쓸 수 있도록 하는 문법
console.log(`안녕하세요~ 저는 ${name}이고, 나이는 ${age}살 입니다.😊`);

console.log(`변수말고 코드 실행도 가능해요 ${4+6}`);


// =================

// 2. 숫자형(number)
// 정수와 실수를 구분하지 않음
const num = 100;
const num2 = 3.14; 
// num2 = 1; < const 써서 이거 안된다.
console.log('숫자형',num, num2);

//====================

// 3. 불리언/논리형(boolean)

// 참 or 거짓을 표현하는 true, false
const isTrue =  true ;
const isFalse = false;
console.log("불리언", isTrue, isFalse);

// ====================

// 4. null (빈 값)
// 의도적으로 값을 비운 상태
// "값이 없음"을 명시 
let isVar = null ; // 진짜 없는 값인지, 
console.log(isVar); 
isVar = "이렇게 이후 값이 할당될 수 있어요.";
console.log(isVar);

//======================

// 5. undefined
// 값을 정의(할당)되지 않은 상태
let x; // undefind 출력
// console.log(x);
// console.log(x2); // 할당되지 않은 변수로 에러 발생


//======================

//[객체 자료형]

// 1. 배열 (array)
let fruits = ["청포도", "오렌지", "체리", "말랑복숭아", "망고스틴"];
console.log('배열',fruits);

//인덱싱
console.log(fruits[3]);
console.log(fruits[-1]); //undefined 출력됨

//at 활용 시 음수 인덱싱 가능
console.log(fruits.at(2)); //체리
console.log(fruits.at(-1)); //망고스틴

fruits[3] = "딱딱복숭아";
console.log(fruits);

// 배열 안에 요소로 배열 넣을 수 있다.
// 변수 자체에 재할당은 불가하나
// 배열 내부의 요소는 수정 가능
const korean = [
    ["가","나","다"],
    ["라","마","바"],
    ["사","아","자"]
];

console.log(korean[0][1]); // 나 , 0번째 인덱스 요소 중 1번 인덱스 요소 출력.
korean[2][2] = '하';
console.log(korean[2][2]); 
// 느슨한 자바 스크립트의 특징에 의해 오브젝트는 주소 값만 유지되면 밸류 값이 바뀌는 건 신경 안 쓴다. 
console.log(korean);
// korean = [
//     [1,2,3],
//     [4,5,6],
//     [7,8,9]
// ] ; //변수를 재 할당하는 건 안됨. const는 도어락 잠긴 집과 비슷해서

korean[0] = [1,2,3];
console.log(korean);

// =============================

// 2. 객체 (object)

// 키-값 쌍을 값으로 가짐
let cat = {
    name: "장화",
    age: 18,
    isCute: true,
    '12': 12,
    mew: function(){
        return "야옹"
    }, //파이썬의 def 와 같은 함수 설정
};

console.log('객체', cat);

// 객체의 값 조회
// 1) 점 표기법
console.log(cat.name);
console.log(cat.age);
// console.log(cat.12); //키가 숫자인 경우 접근 못함

// 2) 대괄호 표기법
console.log(cat['name']);
console.log(cat['age']);
console.log(cat[12]); // 키가 숫자여도 접근 가능 

cat.mew(); // => '야옹'이라는 문자열이 리턴됨 (웹상에 안 보임)
console.log(cat.mew()); //console.log로 해야만 출력됨


let cat2 = {
    name: "장화",
    age: 18,
    isCute: true,
    '12': 12,
    mew: function(){
        alert('야옹22');
    }
};

// cat2.mew()//cat2 라는 객체의 mew키 값을 실행시키는 코드. 함수 안에 저장된 alert(미니창) 작동된다.

let cat3 = {
    name: "장화",
    age: 18,
    isCute: true,
    '12': 12,
    mew: function(str){
        return str;
    }
};

cat3.mew("야옹야옹"); // 매개변수로 전달한 "야옹야옹"을 리턴 < console 에는 안 나옴.
// alert(cat3.mew('야옹야옹'));
// alert(cat3.mew('멍멍'));
// 그러나 디버깅할 때는 실행해버리고 console 확인이 안되니 확인할 거면 console.log 로...

// ============================

// 자료형 확인(typeof)

console.log(typeof '문자'); //string 나옴
console.log(typeof 1124); // number
console.log(typeof 3.14); // number 정수 실수 구분 X
console.log(typeof true); // boolean
console.log(typeof false); // boolean
console.log(typeof null); // object
console.log(typeof undefined); // undefined

// 배열은 object 하위의 array이고, array에는 메서드들이 자동으로 포함되어 typeof로 자료형 확인 시 object로 출력
console.log(typeof fruits); // object
console.log(typeof cat); // object



// 실습 1
console.log('실습 1');
let hu = {
    name: "이몽룡",
    age: 18,
    like: ['강아지','고양이'],
    girlfreind: {
        name: '성춘향',
        age: 16
    },
    isMarried: true
};
console.log(hu);

// 변수 선언 명칭과 가독성만 수정 함...


// ======================================

// 형변환

// 1. 암시적 형변환
console.log('암시적 형변환 (1)', '2' + 3);
// 기대: 2(문자열), 3(숫자)
// 결과: '암시적 형변환 (1)', 23(문자열 합산) 됨.

console.log("암시적 형변환(2)", typeof (100 + '1')); 
// 문자열 + 숫자형은 자료형 타입을 알 수 없어 에러가 나야하나 여기서는 string 타입 뜸.
// JS가 마음대로 변환해버릴 정도로 느슨하다. (특징)

// 2. 명시적 형변환

// 2-1. 문자열 변환: String(), .toString()

let string1 = 123;
let string2 = true;
let string3 = undefined;

console.log('원본 string1',typeof string1);
console.log(String(string1), typeof String(string1)); // 숫자 123이 문자열 "123"으로 변환
console.log(String(string2), typeof String(string2)); // "true"
console.log(String(string3), typeof String(string3)); // "undefined"

// .toString() 사용

console.log(string1.toString(), typeof string1.toString());
console.log(string2.toString(), typeof string2.toString());

//console.log(string3.toString(), typeof string3.toString());
//이건 할당하지 않은 값을 어떻게 메서드 적용하냐며 에러가 남.
// 변수 값이 없기 때문에 변환 불가(내장메서드 사용)

// 2-2. 숫자로 변환: Number(), parseInt()

let number1 = '123';
let number2 = false;
let number3 = '진짜 문자열';
let number4 = 3.14;
let number5 = '3.14';

// Number() 사용
console.log('===');
console.log(Number(number1), typeof Number(number1));
console.log(Number(number2), typeof Number(number2));
// 0 > false는 다르게 표현하면 0이기 때문에 숫자 변환 시 0 출력 (True는 1)
console.log(Number(number3), typeof Number(number3));
// NaN (Not a Number)
console.log(Number(number4), typeof Number(number4)); // 3.14
console.log(Number(number5), typeof Number(number5)); // 3.14

//"정의되지 않음" > 값이 아예 없다. > NaN
console.log(Number(undefined), typeof Number(undefined)); // NaN

//값이 없음을 정의 >  값이 없다는 것을 표현하는 0으로 출력
console.log(Number(null), typeof Number(null));

//tip 선언된 변수 위치 파악하는 법: 컨트롤+ 클릭하면 위치 이동함(클튜 레이어 이동 선택과 유사함)

//parseInt() 사용 > 소수점까지 버리고 정수로 출력
console.log('=== 기능 사용 확인 ===')
console.log(parseInt(number1), typeof parseInt(number1)); // 123
console.log(parseInt(number4), typeof parseInt(number4)); // 3
console.log(parseInt(number5), typeof parseInt(number5)); // 3

console.log(parseInt(3.8), typeof parseInt(3.8)); // 3 > 소숫점 버림.

//parseFloat() 사용 > 소수점까지 모두 변환, 자료형은 number 출력
console.log('=== 기능 사용 확인 ===')
console.log(parseFloat(number4), typeof parseFloat(number4)); // 3.14
console.log(parseFloat(number5), typeof parseFloat(number5)); // 3.14
console.log(parseFloat(3.8), typeof parseFloat(3.8)); // 3.8


// console.log('실습2')
// let mathScore = '77';
// let engScore = '88';

// // 시험 점수 평균 계산하여 avgScore 저장
// // console.log(avgScore) 이용해서 콘솔창에서 확인하도록 프로그램 작성
// // 형변환 사용

// let avgScore = ((Number(mathScore)) + (Number(engScore)) / 2 ;

// console.log(avgScore);


console.log('prompt 활용한 값 입력, 평균 구하기 실습3')
let mathScore = Number(prompt('수학 점수 입력'));
let engScore = Number(prompt('영어 점수 입력'));

let avgScore = (mathScore + engScore) / 2 ;
console.log(avgScore);
