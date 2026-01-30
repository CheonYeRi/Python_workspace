let arr = [10, 20, 30, 40, 50];

console.log('원본 arr: ', arr);
console.log('길이:', arr.length); // 함수 X 요소 기준 세줌

// 요소 추가
arr.push(60); // 배열 가장 마지막에 추가
console.log('push(60)',arr);

arr.push(70,80,90,100);
console.log('push로 다수 추가',arr); // 여러 개 추가 가능

arr.unshift(0);
console.log('unshift(0)',arr); // 배열 맨 앞에 추가. 0 10 20 30...

arr.unshift(-10, -20, -30); // 여러 개 추가 가능하나 매개변수 전달한 순서로 삽입됨
console.log('unshift(변형)',arr);
//[-10, -20, -30, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

// 요소 삭제
let del1 = arr.pop();
console.log('=== arr.pop() ===');
console.log('del1:', del1); // 100 -> arr 배열에서 가장 마지막 요소 삭제한 뒤 **삭제한 요소**를 반환

// arr.pop()이 동작하면서 원본 arr의 가장 마지막 요소인 100이 사라짐
console.log('arr(원본 배열):', arr); // [-10, -20, -30, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

let del2 = arr.shift();
console.log('=== arr.shift() ===');
console.log('del2:', del2); // -10
console.log('arr(원본 배열):', arr); // [-20, -30, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

let arr_copy = arr; // 원본 유지가 필요한 경우에는 이렇게 복사본을 만들어서 해당 복사본으로 배열을 수정

// 슬라이싱
console.log('=== arr.slice(1, 4) ===');
let sliced = arr.slice(1, 4);
console.log('sliced:', sliced);
console.log('arr:', arr); // 원본 유지됨

// splice : 기존 요소를 삭제 or 교체 (원본 변경 O)
console.log('=== arr.splice ===');
arr.splice(1, 5, 15); // 1번째 인덱스부터 요소 5개 삭제, 그 자리에 15 추가
console.log('splice(1, 5, 15):', arr);

arr.splice(2, 2); // 매개변수를 2개만 작성하면, 첫 번째 매개변수 인덱스부터 두 번째 매개변수 갯수까지 삭제만 진행
console.log('splice(2, 2):', arr);

// 결합
let arr2 = [10000, 20000];
console.log('concat:', arr.concat(arr2)); // [-20, 15, 60, 70, 80, 90, 10000, 20000]
console.log('arr 원본:', arr); // 원본 변경 X

//탐색
console.log('indexOf(만):', arr.indexOf('만')); // -1 > 배열 안에 찾는 요소 없으면 -1 반환
console.log('indexOf(10000):', arr.indexOf('10000')); //-1 > 원본 arr에 10000 없음
console.log('indexOf(80):', arr.indexOf('80')); // 4
console.log('원본 arr', arr); // 변경 X

console.log('includes(80)', arr.includes(80)); // 불리언 형태로 포함 여부 표시함
console.log('원본 arr', arr); // 변경 X

// 정렬 (원본 변경O)
let num = [4, 2, 7, 1, 100, 6];
console.log('원본 num', num);

num.sort(); //오름차순
//숫자 크기를 비교하는 게 아닌 문자 기준 앞글자 보고 정렬 <JS 암시적 형변환에 의한 문자열 판정
//만약 4, 400처럼 앞글자 같을 시 다음 두 번째 글자 비교 정렬
console.log('num.sort()', num);

//숫자값 기준으로 정렬하고 싶다면
//사칙연산 사용, JS의 암시적 형변환을 이용하여, 연산자 넣어 숫자로 지시해 정렬 기준 잡은 것
num.sort((a,b) => a-b);

num.sort((a,b) => b - a); //내림차순. 로직 전개가 복잡하니 그냥 이리 생각하자 하심.
//400, 7, 6, 4, 2, 1 결과. b-a는 숫자를 기준으로 정렬해서 숫자 크기 정렬이 된다.
console.log('num.sort((a,b) => b - a)', num);

//예시
let users = [
    {id: 3, name: '레일라'},
    {id: 1, name: '루나'},
    {id: 4, name: 'A씨'},
    {id: 2, name: 'B군'},
];

users.sort((a,b) => a.id - b.id);
//a,b는 요소(고유명사X) a.id (요소에 있는 id 값 기준)
console.log(users);

//배열 순서 뒤집기, 원본 변형O
users.reverse();
console.log('reverse:', users);

// --------------

//배열 순회 메서드
//함수 안에 함수 또 넣는 걸 콜백 함수라고 함.
// 1 map : 배열을 순회하면서 매개변수로 전달받은 콜백함수를 적용(원본 변경 X)
num = num.map((x)=> x*2); //각 요소를 한 번 씩 선택해서 매개변수(x)로 전달하고, 전달받은 x에 2를 곱해서 배열 재할당
console.log(num);

// 2 filter : callback 함수를 기준으로 요소를 필터링해서 반환 (원본 변경 X)
let filtered = num.filter((x) => x > 5);
console.log(filtered);

// 3 reduce : 앞 요소에 대해 뒤 요소를 연산한 결과를 누적
let sum = num.reduce((acc, cur) => acc + cur, 0);
// 두 번째 매개변수로 받은 0에 배열을 순회하면서 앞 요소에 뒷 요소를 더한 값을 반환
console.log(sum); //800

let sum2 = 0;
for (let i = 0; i < num.length; i++) {
    sum2 += num[i];
}
console.log(sum2); // 840

// 4 반복문
let fruits = ['수박', '참외', '귤', '오렌지', '딸기'];

// 4-1 for문 -> 인덱스 기반
//출력 결과
// for문 활용 배열의 1번째 요소 출력: 수박
for (let i = 0; i < fruits.length; i++){
    console.log(`배열 ${i+1}번째 요소 출력: ${fruits[i]}`);
}

// 4-2 for of 문
for (let fruit of fruits) { //fruits라는 배열로 부터(of) 해병 배열의 요소들을 fruit라고 부르며 배열 순회함
    console.log(`for of문 활용 배열의 fruit 출력:${fruit}`);
}

// 5. 배열 메서드 forEach
fruits.forEach((fruit, index) => 
    console.log(`forEach 활용 배열의 ${index}번째 요소 출력: ${fruit}`)
);
//순서가 중요하기 때문에 f, i 매개변수 명칭을 써도 적용된다.
//요소 명, 인덱스 위치, 배열 로 지정되고 2, 3번 째 변수는 생략 가능하다.


console.log('=== 실습 1 ===');
// 1 ~ 100 까지 배열을 for문을 사용해서 만들고 배열의 합 구하기.
let numbers = []; // 정수 생성

for (let i = 1; i <= 100; i++){
    numbers.push(i);
}
console.log('원본 배열',numbers);

let i_sum = 0;
for (let num of numbers) {
    i_sum += num;
}

let i_sum1 = 0;
numbers.forEach((n) => i_sum1 += n);

// reduce 활용
let i_sum2 = numbers.reduce((acc, cur) => acc + cur);
console.log(i_sum2)

console.log('=== 실습 2 ===');

let fruits1 = ["사과", "딸기", "파인애플", "수박", "참외", "오렌지", "자두", "망고"];
let fruits2 = ["수박", "사과", "참외", "오렌지", "파인애플", "망고"];
// 두 배열에서 동일한 요소만을 가지는 배열 same 만들기
// 두 배열에서 다른 요소만을 가지는 배열 diff 만들기
// filter : callback 함수를 기준으로 요소를 필터링해서 반환 사용


//오퍼레이터 파트 참고, 
let same = fruits1.filter((fruit) => fruits2.includes(fruit));
console.log('same 배열 출력:',same);

let diff = fruits1.filter((fruit) => !fruits2.includes(fruit));
console.log('diff 배열 출력:',diff); // 부정연산자 사용

console.log('=== 실습 3 ===');
// 평일/ 주말 구분
//JS 내장된 Date 객체 활용
//Date.getDay(): 요일별로 0-6(일~토)로 숫자 변경
let now = new Date();
console.log(now.getDay()); // 금요일 기준 5

let nowDay = new Date().getDay();

// switch
switch (nowDay) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        console.log('평일');
        break;
    case 6:
    case 0:
        console.log('주말');
    default:
        console.log('알 수 없음');
        break;
}
//if - else if 문
if (nowDay === 0 ){
    console.log('주말');
} else if (nowDay === 1){
    console.log('평일');
} else if (nowDay === 2){
    console.log('평일');
} else if (nowDay === 3){
    console.log('평일');
} else if (nowDay === 4){
    console.log('평일');
} else if (nowDay === 5){
    console.log('평일');
} else if (nowDay === 6){
    console.log('주말');
}

//if - else 문

if(nowDay === 5 || nowDay === 1 || nowDay === 2 || nowDay === 3 || nowDay === 4){
    console.log('평일');
} else {
    console.log('주말');
}

//삼항연산자
let today = nowDay === 0 || nowDay === 6
    ? '주말' : '평일';
console.log(today) 

console.log('=== 실습 4 ===');
// 0 ~ 10 사이의 랜덤 숫자 출력
// Math.random(): 0 이상 1 미만의 난수 생성
// Math.floor(x): 양수 기준으로는 소숫점 버림, 음수 기준으로는 더 작은 음수로 소숫점 사라짐
    // Math.floor(3.298405) - > 3 (소숫점 버림)
    // Math.floor(-3.298405) - > -4 ::바닥으로 내린다는 맥락대로 더 낮은 값이 됨.

console.log(Math.floor(Math.random() * 11));
//0.2 * 10 = 2 , 0.354 * 10 = 3.54... 
// Math.random() * 10 은 0이상 10미만의 결과 출력
// 0 ~ 10 사이 얻기 위해서는, * 11 해야한다. 무조건 11 미만 숫자가 나오기 때문에
// Math.floor 사용하면 0 ~ 10으로 반환 시켜준다.