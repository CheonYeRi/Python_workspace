-- DDL (Data Definition Language)
-- 데이터 베이스, 테이블을 정의하는 언어

-- 1. CREATE
CREATE DATABASE test_db;
DROP DATABASE test_db;

-- 인코딩 저장
CREATE DATABASE test_db CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb8_unicode_ci;

USE test_db;
-- 해당 테이블로 지정

CREATE TABLE user (
	cust_id CHAR(10) NOT NULL PRIMARY KEY,
    cust_name VARCHAR(10) NOT NULL,
    adrress CHAR(10) NOT NULL,
    phone CHAR(11),
    birth DATE
);
- 테이블 생성

SHOW TABLES;
-- 테이블 보여주기
DESC user;
-- 적용

-- ALTER
-- 1. 속성 추가
ALTER TABLE user ADD age INT;

-- 2. 컬럼 자료형 수정
ALTER TABLE user MODIFY address VARCHAR(40);
-- 3.컬럼 이름 수정
ALTER TABLE user RENAME COLUMN address TO user_address;
-- 4. 컬럼 삭제
ALTER TABLE user DROP adrress;


-- 실습 사용한 관계성 연결포함 생성 테이블 코드
CREATE TABLE orders (
	order_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cust_id CHAR(10) NOT NULL ,
    prod_name CHAR(6) NOT NULL,
    price INT NOT NULL,
    amount SMALLINT NOT NULL,
    FOREIGN KEY (cust_id) REFERENCES user(cust_id)
);


-- 1. SELECT 기본 문법

-- 모든 컬럼 선택
SELECT * FROM class;

-- 일부 컬럼만 선택
SELECT class_name,category FROM class;

-- 2.WHERE
SELECT * FROM student WHERE name = "이지은";
SELECT * FROM student WHERE student_id = 10;

--조건 선택
SELECT name, age FROM student WHERE age >= 25;
SELECT name, age FROM student WHERE age >= 25 AND age <= 27;

SELECT name, age FROM student WHERE class_id IN ('CLS01', 'CLS02','CLS03');

SELECT * FROM student WHERE name LIKE '이%';

SELECT * FROM class WHERE category LIKE "%엔드";

SELECT * FROM student WHERE join_date LIKE "%04%";


-- 3. ORDER BY 정렬
SELECT name, age FROM student ORDER BY age;
SELECT name, age FROM student ORDER BY age DESC;

SELECT class_id, class_name, start_date FROM class ORDER BY class_name;
SELECT class_id, class_name, start_date FROM class 
WHERE category LIKE "%엔드%" ORDER BY class_name;

SELECT student_name , gender FROM student ORDER BY gender, student_name;

-- 4. LIMIT
SELECT * FROM student LIMIT 3;

SELECT * FROM student ORDER BY age LIMIT 5;

-- 5. 중복 제거
SELECT DISTINCT gender FROM student;

-- 6. GROUP BY, HAVING
USE my_shop;

SELECT cust_id,amount FROM orders ORDER BY cust_id;

SELECT cust_id "고객 아이디", sum(amount) "총 구매 개수" FROM orders GROUP BY cust_id;

SELECT cust_id "고객 아이디", sum(amount * price) "총 구매 금액" FROM orders 
GROUP BY cust_id;
ORDER BY sum(amount * price) DESC;


SELECT COUNT(*) FROM customer;

SELECT * FROM customer;
USE codingon_db;
SELECT COUNT(*) "나이가 입력된 수" FROM student WHERE age IS NOT NULL;

-- 그룹화 이전은 WHERE, 이후에는 HAVING 사용함.


-- 수정
SELECT * FROM student;
UPDATE student SET age = 26 WHERE student_name="정국";

UPDATE student SET age = age + 1 WHERE class_id ="CLS01" and age < 25;

SELECT * FROM class;

DELETE FROM class WHERE room LIKE "G%";

-- edit - 프리퍼런스 - SQL 부분에서 보호모드 꺼야 수정됨