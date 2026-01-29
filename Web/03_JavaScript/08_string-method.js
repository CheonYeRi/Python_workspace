let str = "  Hello JavaScript World  ";

console.log('원본 str', str);

// 1 .length
console.log('길이', str.length); //함수 x 하나의 속성

// 2 .trim(): 공백 제거해줌.
console.log('공백제거', str.trim()); //문자열 양 끝 공백 제거
console.log('원본 str', str); //원본 변경이 없다.

// 대소문자 변환
console.log('대문자 변환:', str.toUpperCase()); // 공백 유지 전부 대문자    HELLO JAVASCRIPT WORLD  
console.log('원본 str', str); //변경 X

//소문자 변환
console.log('소문자 변환', str.toLowerCase()); //   hello javascript world 
console.log('원본 str', str); // 변경 x 

// 탐색
// 인덱스 결과에 -1은 없는 글자라고 표시한다. // 매개변수로 받은 문자열이 없다면.
console.log('인덱스 찾기', str.indexOf('J')); // 8, j로 소문자 쓸 시 -1로 없다 뜸.
console.log('인덱스 찾가', str.indexOf('Java')); // 8, 매개변수 첫 글자 기준으로 인덱스 표시함

console.log('문자열의 포함 여부 확인', str.includes('Java')); // true , false 불리언으로 반환
//.indexOf()로도 문자열에 포함 여부를 -1로 알 수 있긴 하다.
console.log('문자열의 포함 여부 확인', str.includes('jav'));

// 슬라이싱
console.log('슬라이싱', str.slice(8,18)); //JavaScript, 8인덱스부터 17인덱스까지 출력
console.log('원본 str', str); // 변경 x

//치환
console.log('한 글자 치환:', str.replace('a','e')); 
// 문자열 중에서 가장 처음 나오는 a글자를 e로 치환 Hello JevaScript World
console.log('한 단어 치환', str.replace('World','Universe')); // 단어 치환 가능
console.log('전부 치환', str.replaceAll('l','v')); // Hevvo JavaScript Worvd 
console.log('원본 str', str); //변경 x

//분할
console.log('""기준 분할', str.split(''));
//''(공백)을 매개변수로 전달 시, 모든 글자들이 하나씩 잘려 배열로 반환
console.log('" "기준 분할', str.split(' ')); // ' '(공백 한 칸)을 기준으로 문자열을 나눠서 배열 반환
//['', '', 'Hello', 'JavaScript', 'World', '', '']
console.log('l 기준 분할:', str.split('l')); //['  He', '', 'o JavaScript Wor', 'd  ']
//분할하는 기준인 매개변수는 사라지고, 배열로 만들어져 반환
console.log('원본 str', str); // 변경 X

//합치기
let str2 = "with JavaScript";
console.log('문자열 합치기:', str.concat(str2)); // str + str2 순으로 합쳐짐(공백 포함)

console.log(`문자열 합치기2, ${"Hello ".concat(str2)}`); //문자열에 공백 없이 바로 합쳐짐 (공백 포함해야 띄어씀)
console.log(`문자열 합치기3, ${"Hello ".concat(str2, str)}`);
//with JavaScript  Hello JavaScript World
console.log(`문자열 합치기4, ${"Hello ".concat("I'm Layla")}`);
//Hello I'm Layla
console.log('원본 str', str);
console.log('원본 str2', str2);
//원본 변경 X

