SELECT employee_id, name, (SELECT COUNT(reports_to)
FROM Employees
WHERE reports_to = E.employee_id) as reports_count,
(SELECT ROUND(AVG(age))
FROM Employees
WHERE reports_to = E.employee_id) as average_age
FROM Employees E
WHERE employee_id IN (SELECT reports_to FROM Employees)
ORDER BY employee_id