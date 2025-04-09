# Write your MySQL query statement below
SELECT name, SUM(amount) as balance
FROM Users U
JOIN Transactions T
ON U.account = T.account
GROUP BY name
HAVING SUM(amount)>10000