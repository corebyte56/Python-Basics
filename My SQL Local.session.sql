CREATE DATABASE Collage;

USE Collage;

CREATE TABLE Student(
	Id INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT NOT NULL
);

INSERT INTO Student VALUES(1, "Fahim", 19);
INSERT INTO Student VALUES(2, "shimul", 21);
INSERT INTO Student VALUES(3, "sufe", 15);
INSERT INTO Student VALUES(4, "sabbir", 20);

SELECT * FROM Student;

DROP TABLE Student;

CREATE TABLE People(
    PersonID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE
);


INSERT INTO People VALUES   (1, 'John', 'Doe', '1990-01-01');
INSERT INTO People VALUES   (2, 'atik', 'khan', '2010-01-01');
INSERT INTO People VALUES   (3, 'rubel', 'shikder', '2001-01-01');
INSERT INTO People VALUES   (4, 'shimul', 'islam', '2000-01-01');
INSERT INTO People VALUES   (5, 'fahim', '$$$', '2003-01-01');
INSERT INTO People VALUES   (6, 'faisal', 'pagla', '2004-01-01');
INSERT INTO People VALUES   (7, 'awlad', 'hossain', '2007-01-01');

SELECT * FROM People;



CREATE DATABASE IF NOT EXISTS CompanyDB;