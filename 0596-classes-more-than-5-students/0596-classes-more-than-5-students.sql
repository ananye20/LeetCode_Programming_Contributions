# Write your MySQL query statement below
SELECT distinct class
FROM Courses
GROUP BY class
HAVING count(class)>=5