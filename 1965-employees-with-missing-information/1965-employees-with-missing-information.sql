# Write your MySQL query statement below
SELECT E.employee_id
FROM Employees E
LEFT JOIN Salaries S
ON E.employee_id = S.employee_id
WHERE salary is NULL or name is NULL
UNION
SELECT S.employee_id
FROM Employees E
RIGHT JOIN Salaries S
ON E.employee_id = S.employee_id
WHERE salary is NULL or name is NULL
ORDER BY employee_id