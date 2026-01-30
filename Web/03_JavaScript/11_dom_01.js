// script 태그 위치가 head > title 아래였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head태그
console.log(document.body); // null 나옴.
// html도 위에서부터 코드가 순차적으로 실행되기 때문에
// js를 불러온 뒤에 body 태그가 생성되어서 body가 null 변환 됨

// script 태그 위치가 html 닫히는 태그 위였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head태그
console.log(document.body); // body 태그 나온다
// body가 생성된 이후 js 코드를 불러오기에 문제 없이 작동되는 것

//이런 script의 불편함을 개선하고자
// script 태그에 type ="module" 속성을 부여할 경우
// html이 모두 로드된 뒤 js 불러와 실행
// 현재 html에 적힌 태그 형태는 아래와 같다.
// <script type="module" src="./11_dom_01.js"></script>
// 위치 head태그 내부 title 아래

//document 객체를 활용한 HTML 요소 선택
// 이전 방식(legacy)
console.log(document.getElementById('green'));
// 여러개 출력되는 명령어는 Elements(복수형)이 붙어있다.
console.log(document.getElementsByClassName('default'));
console.log(document.getElementsByTagName('div'));

console.log('----------------------');
//선호되는 방식
//querySelector
//CSS 선택자로 HTML 요소를 가져옴
//제일 처음 발견한 요소 하나만 반환
console.log(document.querySelector('#green')); //CSS 선택자 양식 참고
console.log(document.querySelector('.default'));
console.log(document.querySelector('input'));
console.log(document.querySelector('[name="id"]')); // 속성 선택자 양식

console.log('----------------------');

//querySelectorAll
// CSS 선택자에 만족하는 모든 HTML 요소들을 NodeList라는 배열과 유사한 형태로 반환
// 불러온 요소들에 대한 순회가 가능 (forEach활용)
console.log(document.querySelectorAll('.default'));
console.log(document.querySelectorAll('.others'));
console.log(document.querySelectorAll('div'));

// forEach 활용 NodeList 순회
const divEl = document.querySelectorAll('div');
console.log('querySelectorAll 활용 모든 div요소 선택:',divEl);
divEl.forEach((el) => console.log(el));

// for of 활용 NodeList 순회
const classDefaultEl = document.querySelectorAll('.default');
for (let el of classDefaultEl){
    console.log('for of 활용 .default 요소 순회:', el);
}