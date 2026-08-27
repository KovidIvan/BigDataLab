-- 1
SELECT ProjectName
FROM projects p
JOIN employeeprojects ep ON p.ProjectID = ep.ProjectID
JOIN employees e ON ep.EmployeeID = e.EmployeeID
WHERE e.FirstName = 'Bob'
  AND e.LastName = 'Johnson'
  AND ep.HoursWorked > 150;
--2
SELECT * FROM projects;
UPDATE projects p 
SET Budget = Budget*1.1 
WHERE p.projectid IN (
	SELECT ep.projectid
	FROM employeeprojects ep
	JOIN employees e ON ep.employeeid = e.employeeid 
	WHERE e.department = 'IT'
	);
SELECT * FROM projects;
--3
UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;

--4
BEGIN;
WITH new_employee AS (
    INSERT INTO Employees (FirstName, LastName, Department, Salary)
    VALUES ('John', 'Doe', 'IT', 70000.00)
    RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 
    ne.EmployeeID,
    (SELECT ProjectID FROM Projects WHERE ProjectName = 'Website Redesign'),
    80
FROM new_employee ne;
COMMIT;

SELECT * FROM Employees WHERE FirstName = 'John' AND LastName = 'Doe';
SELECT * FROM EmployeeProjects WHERE EmployeeID = (SELECT EmployeeID FROM Employees WHERE FirstName = 'John' AND LastName = 'Doe');
