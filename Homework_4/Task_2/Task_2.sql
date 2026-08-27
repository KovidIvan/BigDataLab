CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY ,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
Location VARCHAR(50)
);

SELECT * FROM Departments

ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);

UPDATE Employees 
SET Email = LOWER(firstname) || '.' || LOWER(lastname) || '@company.com'
WHERE Email IS NULL;

ALTER TABLE Employees ADD CONSTRAINT UQ_Email UNIQUE (Email);

ALTER TABLE Departments RENAME COLUMN Location TO OfficeLocation;

SELECT * FROM Employees