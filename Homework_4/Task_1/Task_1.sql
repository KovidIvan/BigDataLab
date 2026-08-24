INSERT INTO Employees (firstname, lastname, department, salary)
VALUES 
    ('John', 'Doe', 'Finance', 55000.00),
    ('Jane', 'Smith', 'HR', 60000.00);


SELECT * FROM Employees;

SELECT firstname, lastname 
FROM Employees 
WHERE department = 'IT';


UPDATE Employees 
SET salary = 65000.00 
WHERE firstname = 'Alice' AND lastname = 'Smith';


DELETE FROM Employees 
WHERE firstname = 'Eve' AND lastname = 'Davis';


SELECT * FROM Employees;