CREATE DATABASE codingon_db CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;

USE codingon_db;

CREATE TABLE class ( 
	class_id CHAR(5) NOT NULL,
    class_name VARCHAR(30) NOT NULL,
    category VARCHAR(20) NOT NULL,
    room CHAR(5) NOT NULL,
    start_date DATE
);

CREATE TABLE student ( 
	student_id INT NOT NULL AUTO_INCREMENT,
    class_name VARCHAR(20) NOT NULL,
    age INT,
    gender ENUM('M','F'),
    class_id CHAR(5) NOT NULL,
	PRIMARY KEY (class_id),
    FOREIGN KEY (class_id) REFERENCES class(class_id),
    join_date DATE 
);


insert into class (class_id, class_name, category, room, start_date) VALUES
('CLS01', '프론트엔드 12기', '프론트엔드', 'B-101', '2024-01-08');