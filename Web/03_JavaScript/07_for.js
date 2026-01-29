// 1. for 문
// 횟수를 기준으로 하는 반복문

console.log('=== for문 ===');

// i요소는 0부터 시작해서 ; i가 10까지 ; i에 1씩 증감한다; (시작조건;끝조건;배율)
for(let i = 0; i < 10; i++) {
    console.log(i);
}

console.log('---------');

for (let i = 0; i <= 10; i++) {
    console.log(i);
}

for (let i = 10; i >= 1; i--) {
    console.log(i);
}

for (let i = 0; i <= 20; i+=3) {
    console.log(i);
}

console.log('---------');

// 1부터 100까지 합 구하기

let sum = 0;
// 변수 선언을 먼저 해둬야 합산을 하든 뭐든 계산식이 들어감.

for (let i = 1; i < 101; i++){
    sum += i;
    console.log(sum);
}

console.log('1~100까지의 합',sum);

console.log('=== 실습 1 ===');
// 10000까지의 숫자 중에서 13 배수면서 홀수인 숫자 찾기.
// prompt를 이용해서 입력받은 수 까지의 13 배수면서 홀수인 숫자 찾기
// 13의 배수를 찾는 건 연산자(나머지) 사용함

// 1부터 시작해도 되는데 13배수가 조건이니 13부터 함
for (let i = 13; i < 10001; i++){
    if(i % 13 === 0 && i % 2 === 1) {
        //i % 13 === 0 -> 13의 배수
        //i % 2 === 1 -> 홀수
        console.log(i);
    }
}

// 입력 받아 출력하는 프로그램 출력
console.log('=== 실습 1 추가 ===');
let count = Number(prompt('범위를 입력하세요'))

console.log(`1~${count} 사이에서 13배수이며 홀수 찾기`)

for (let i = 1; i < count; i++){
    if(i % 13 === 0 && i % 2 === 1) {
        console.log(i);
    }
}


// 이중 for 문
console.log('=== 이중 for문 ===');
//변수 const는 사용할 수 없다
for (let i = 0; i < 3; i++){
    for(let j = 0; j < 5; j++){
        console.log('i:', i, 'j', j);
    }
    // i는 고정된 상태로 j만 커지면서 해당 scope의 코드 실행
    // j의 루프가 완료되면 i가 1 커진다.
}

console.log('=== 실습2 ===');

for (let i = 0; i < 10; i++){
    console.log(`=== ${i}단 ===`)
    for (let j = 1; j < 10; j ++){
        console.log(`${i} x ${j} = ${i * j}`)
    }
}

// 2. while 문
// 조건을 기준으로 한 반복
console.log('=== while 문 ===');

let i = 0;


// //무한 루프 됨 (i가 계속 0 되니까)
// while(i<5){
//     console.log(i);
// }

while(i < 5){
    console.log(i);
    i++;
}

//초록불일 때만 콘솔을 찍는 로직
let blinker = '초록불';

while (blinker === '초록불'){
    console.log('길을 건너세요');
    blinker = prompt('신호등 상태 입력(초록불/빨간불)');
    //예외 처리
    if (blinker === '초록불'){
        continue; // 초록불이면 while문 반복
    } else if (blinker === '빨간불'){
        break; //루프 탈출 코드
    } else{
        blinker = prompt('신호등 신호 다시 입력하세요(초록불/빨간불)');
    }

}

console.log('=== 실습 3 ===');
//0 ~ 100 사이 숫자중 2 또는 5배수의 총합 구하기
let total = 0; // 합
let Count = 0; // for문에서 i 역할(반복 횟수)

while(Count <= 100) {
    if (Count % 2 === 0 || Count % 5 === 0){
        total += Count;
    }
    Count++;
}

console.log('0 ~ 100까지의 합',total);