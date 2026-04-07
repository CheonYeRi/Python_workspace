CREATE DATABASE my_shop CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;

USE my_shop;

SHOW TABLES;
-- 테이블 보여주기
DESC cusm

DROP DATABASE my_shop;
-- 데이터베이스 삭제

ALTER TABLE user RENAME COLUMN adrress TO user_address;
--테이블 생성

CREATE TABLE customer (
	cust_id CHAR(10) NOT NULL PRIMARY KEY,
    cust_name VARCHAR(10) NOT NULL,
    adrress CHAR(10) NOT NULL,
    phone CHAR(11),
    birth DATE
);

CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT,
	cust_id CHAR(10) NOT NULL,
    prod_name CHAR(6) NOT NULL,
    price INT NOT NULL,
    amount SMALLINT NOT NULL,

    PRIMARY KEY (order_id), --기본 키 설정
    --cust_id를 customer 테이블의 cust_id와 외래키로 연결
    FOREIGN KEY (cust_id) REFERENCES customer(cust_id) 
);

-- INSERT
insert into user (cust_id, cust_name, address, phone, birth)
values ('C001', '김민수', '서울시', '01012345678', '1990-05-14');
-- 지정생성

insert into user values ('C002', '이영희', '부산시', '0102345689','1985-08-22');
-- 자동생성

insert into user (cust_id, cust_name, user_address, phone, birth) VALUES
('C003', '박철수', '대전시', '01034567890', '1992-11-02'),
('C004', '정유진', '광주시', '01045678901', '1998-01-19'),
('C005', '한지민', '수원시', '01056789012', '1996-06-30'),
('C006', '최우성', '서울시', '01067890123', '1989-03-15'),
('C007', '장윤아', '대구시', '01078901234', '1994-10-05'),
('C008', '오태식', '인천시', '01089012345', '1987-02-25'),
('C009', '류수정', '서울시', '01090123456', '1995-07-08'),
('C010', '배진영', '부산시', '01001234567', '1993-12-12');

select * from orders


INSERT INTO orders (cust_id, prod_name, price, amount) VALUES
('C001', '커피머신', 120000, 1),
('C003', '노트북', 950000, 1),
('C002', '헤드폰', 85000, 2),
('C001', '모니터', 250000, 1),
('C005', '의자', 130000, 1),
('C004', '키보드', 45000, 2),
('C007', '마우스', 32000, 3),
('C009', '조명등', 28000, 1),
('C008', '휴대폰', 990000, 1),
('C010', '게임기', 480000, 1);