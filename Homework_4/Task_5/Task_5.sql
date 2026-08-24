CREATE OR REPLACE FUNCTION CalculateAnnualBonus (employee_id int, salary decimal)
	RETURNS decimal AS $$
	BEGIN
		RETURN salary * 0.1;
	END;
	$$ LANGUAGE plpgsql;

	
SELECT 
    EmployeeID,
    FirstName,
    LastName,
    Department,
    Salary,
    CalculateAnnualBonus(employeeID, salary)
FROM Employees;

CREATE OR REPLACE VIEW IT_Department_View AS
	SELECT
		 EmployeeID,
    	FirstName,
    	LastName,
    	Salary
    FROM Employees
    WHERE Department = 'Senior IT';
SELECT * FROM IT_Department_View;

