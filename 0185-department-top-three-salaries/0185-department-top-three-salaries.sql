WITH cte as(SELECT E.id, E.name as Employee, D.name as Department, salary as Salary, departmentId, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rnk
FROM Employee E
LEFT JOIN Department D
ON E.departmentId = D.id)

SELECT Department, Employee, Salary
FROM cte
WHERE rnk<=3
ORDER BY departmentId, Salary DESC

