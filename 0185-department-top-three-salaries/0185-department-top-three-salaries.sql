# Write your MySQL query statement below
WITH cte AS(SELECT E.id as id, E.name as Employee, salary as Salary, departmentId, D.name AS Department, DENSE_RANK() OVER (PARTITION BY D.id ORDER BY salary DESC) AS rnk
FROM Employee E
JOIN Department D
ON E.departmentId = D.id)
SELECT Department, Employee, Salary
FROM cte
WHERE rnk<=3