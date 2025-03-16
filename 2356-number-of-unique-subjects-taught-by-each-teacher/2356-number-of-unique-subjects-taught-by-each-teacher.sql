# Write your MySQL query statement below
SELECT teacher_id, COUNT(distinct subject_id) as cnt
FROM Teacher
GROUP BY teacher_id