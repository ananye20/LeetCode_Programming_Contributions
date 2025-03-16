# Write your MySQL query statement below
SELECT 
    M.reports_to AS employee_id,
    E.name AS name,
    COUNT(M.employee_id) AS reports_count,
    ROUND(AVG(M.age), 0) AS average_age
FROM 
    Employees M
JOIN 
    Employees E
ON 
    M.reports_to = E.employee_id
GROUP BY 
    M.reports_to, E.name
HAVING 
    COUNT(M.employee_id) > 0
ORDER BY employee_id
