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
//map : 배열을 순회하면서 매개변수로 전달받은 콜백함수를 적용(원본 변경 X)
num = num.map((x)=> x*2); //각 요소를 한 번 씩 선택해서 매개변수(x)로 전달하고, 전달받은 x에 2를 곱해서 배열 재할당
console.log(num);

// filter : callback 함수를 기준으로 요소를 필터링해서 반환 (원본 변경 X)
let filtered = num.filter((x) => x > 5);
console.log(filtered);

//reduce : 앞 요소에 대해 뒤 요소를 연산한 결과를 누적
let sum = num.reduce((acc, cur) => acc + cur, 0);
// 두 번째 매개변수로 받은 0에 배열을 순회하면서 앞 요소에 뒷 요소를 더한 값을 반환
console.log(sum); //800

let sum2 = 0;
for (let i = 0; i < num.length; i++) {
    sum2 += num[i];
}
console.log(sum2); // 840