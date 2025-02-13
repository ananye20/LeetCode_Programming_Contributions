# Write your MySQL query statement below
SELECT S.user_id, IFNULL(ROUND(SUM(CASE WHEN action='confirmed' THEN 1 ELSE 0 END)/COUNT(S.user_id),2),0) as confirmation_rate
FROM Confirmations C
RIGHT JOIN Signups S
ON C.user_id = S.user_id
GROUP BY S.user_id