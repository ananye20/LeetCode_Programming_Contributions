# Write your MySQL query statement below
SELECT employee_id, (CASE WHEN (name LIKE "M%") OR (employee_id%2=0) THEN 0
ELSE salary END) as bonus
FROM Employees
ORDER BY employee_id