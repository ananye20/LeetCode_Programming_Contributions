# Write your MySQL query statement below
WITH cte as (SELECT id, LAG(num) OVER (ORDER BY id) as num2, num
FROM Logs),

abc as(SELECT id, LAG(num2) OVER (ORDER BY id) as num3, num2, num
FROM cte)

SELECT DISTINCT num as ConsecutiveNums
FROM abc
WHERE num=num2 AND num2=num3
