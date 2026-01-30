// greeting이라는 클래스를 가진 요소를 greetingEl 변수에 저장하고 콘솔에 출력하기
let greetingEl = document.querySelector('.greeting');
console.log(greetingEl);

// 태그 내용 출력
// 수정, 불러오기 다 같은 걸 공유 함.
console.log(greetingEl.innerHTML);
console.log(greetingEl.textContent); //태그 안 쪽을 불러올 때 더 선호되는 방식

// 태그 내부 내용 변경
greetingEl.innerHTML = '안녕하세요! 행복한 금요일 조금만 더 <b>힘</b>을 내요!'; // 값을 재할당
//innerHTML: 태그 안 쪽 HTML을 주입 (HTML 양식 반영 O)
greetingEl.textContent = '<b>화이팅!</b>';
//textContent: 태그 안 쪽 문자열을 입력 (HTML 반영 X)
//위에서 아래로 순차 진행해서 가장 마지막 쓴 게 적용된 거다.

//-------

// 속성 변경

const naverEl = document.querySelector('#naver');
naverEl.textContent = '구글';
naverEl.setAttribute('href','https://www.google.com');
console.log(naverEl);
//<a href="https://www.google.com" id="naver">구글</a>
naverEl.setAttribute('id','google'); // 키 - 값 구조와 유사함
console.log(naverEl);


// -------

// 속성값 가져오기
const grapeEl = document.querySelector('#grape');
const grapeUrl = grapeEl.getAttribute('src');
console.log(grapeUrl);

// id가 test인 img태그를 포도 이미지가 보이도록 src 속성 수정하기
const testEl = document.querySelector('#test');
testEl.setAttribute('src', grapeUrl);

//CSS 지정
const fruitsLi = document.querySelectorAll(".fruit");
console.log(fruitsLi[0]); //인덱스 지정 호출, NodeList 형태로 반환

fruitsLi[0].style.backgroundColor = 'red'; //카멜네임 방식으로 지정해야함
//fruitsLi의 첫 번째 태그의 스타일 속성에서 backgroundColor를 red로 지정
fruitsLi[1].style.fontSize = '30px';

// for of 문 활용 모든 fruitsLi 요소 순회- 스타일 지정
for (let el of fruitsLi){
    el.style.backgroundColor = 'skyblue';
    el.style.fontSize = '20px';
    el.style.fontWeight = 'bold';
}

// classList 활용
const h1El = document.querySelector('h1');
h1El.classList.add('title');
console.log(h1El);

//title 클래스 포함 여부 확인 후 불리언으로 반환
console.log(h1El.classList.contains('title'));

h1El.classList.remove('title');
console.log(h1El.classList.contains('title'));
// JS는 빠르게 처리하다보니 출력 오류가 생길 수 있어 포함여부 확인이 정확하다

console.log('---------');
h1El.classList.toggle('title'); //title 클래스가 없다면 추가, 있다면 삭제
console.log(h1El.classList.contains('title')); // T

h1El.classList.toggle('title'); 
console.log(h1El.classList.contains('title')); // F

if (h1El.classList.contains('title')){
    console.log('이건 타이틀');
} else {
    console.log('이건 타이틀 아님.');
}

// ----------------

// 요소 조회
const fruitsEl = document.querySelector('#fruits');

// 자식 요소 조회
console.log('자식 요소 조회',fruitsEl.children);
console.log('1번 인덱스 자식 요소 조회',fruitsEl.children[1]);
//인덱스로 접근 가능, 배열처럼 생겼다.

// 형제 요소 조회
const stEl = document.querySelector('#sb');

console.log('#sb 이전 요소', stEl.previousElementSibling); // 사과 태그 출력
console.log('#sb 다음 요소', stEl.nextElementSibling); //포도 태그 출력
console.log('#sb 다다음 요소', stEl.nextElementSibling.nextElementSibling); // 수박 태그
// 체인링을 해서 연쇄 작동 할 수 있으나 지정 선택 접근이 효율적이다.


// ---------------

// 새로운 요소 생성
const newLi = document.createElement('Li');
newLi.textContent = "만들어진 li";
console.log(newLi);

console.log(document.body); 
// X createElement는 하나의 태그를 생성할 뿐 HTML에는 삽입되지 않음.

// //요소 삽입
// //fruitsEl.append(newLi); // fruitsEl라는 요소에 자식 중 가장 마지막으로 newLi가 삽입
// //fruitsEl.appendChild(newLi); // 위와 동일하게 동작함.

// //append 와 appendChild 차이
// fruitsEl.append('문자열 추가 가능');
// //fruitsEl.appendChild('문자열 추가 불가');

// fruitsEl.append(newLi, newLi, newLi); // 여러 요소를 한 번에 삽입 가능
// //fruitsEl.appendChild(newLi, newLi, newLi); // 여러 요소를 한 번에 삽입 불가

// append()가 더 최신 메서드여서, 현재는 더 선호되고 있다.

fruitsEl.prepend(newLi); // fruitsEl라는 요소에 자식 중 가장 처음으로 newLi 삽입

// 선택한 요소에 형제로 새로운 요소 추가
fruitsEl.before(newLi);
console.log(document.body);

fruitsEl.after(newLi);
console.log(document.body);

//지정한 곳에 감싸고 있는 안 쪽 목록들은 자식, 감싸고 있는 것의 이름은 부모
//부모 근처의 존재는 형제. 지정한 것보다 바깥인 body는 조상이 된다.

//요소 삭제
const firstChild = document.querySelector("#fruits > li"); // <li class="fruit">사과</li>
fruitsEl.removeChild(firstChild); //사과 li 삭제됨
//내 자식들 중 하나 지움.

//자기 자신 삭제
fruitsEl.remove(); // 전부 삭제


console.log('실습1')

// 새로운 요소 생성
const newSp = document.createElement('span');
newSp.textContent = "민트 초코는 맛있다.";
console.log(newSp);
fruitsEl.before(newSp);
console.log(document.body);
