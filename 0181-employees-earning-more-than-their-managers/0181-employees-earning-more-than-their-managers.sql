SELECT E.name AS Employee
FROM Employee E
JOIN Employee M
ON E.managerId = M.id
WHERE E.salary > M.salary;