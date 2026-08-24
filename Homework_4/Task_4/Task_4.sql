SELECT * FROM employees;
UPDATE Employees
SET 
	salary = salary * 1.1
WHERE
	department = 'HR';


SELECT * FROM employees;
UPDATE employees
SET 
	department = 'Senior IT'
WHERE
	salary > 70000;

SELECT * FROM employees;
	DELETE FROM Employees
	WHERE
		EmployeeID NOT IN (
			SELECT
				EmployeeID 
			FROM
				EmployeeProjects
			);
	SELECT * FROM employees;


SELECT * FROM projects;
SELECT * FROM employeeprojects;
BEGIN;
	INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
	VALUES ('CoolProject',137000,'2026-01-15', '2026-06-30');
	
	SAVEPOINT ProjectCreated;
	
	INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
	VALUES (3,4,100),
		   (4,4,120);
COMMIT;
SELECT * FROM projects;
SELECT * FROM employeeprojects;