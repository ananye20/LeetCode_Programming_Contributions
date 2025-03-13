# Write your MySQL query statement below
SELECT name
FROM Employee
WHERE id IN (SELECT managerId as id FROM Employee
GROUP BY managerId
HAVING COUNT(managerId)>=5)