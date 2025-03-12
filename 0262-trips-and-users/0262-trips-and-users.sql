# Write your MySQL query statement below
SELECT request_at as Day, ROUND(SUM(CASE WHEN status!='completed' THEN 1 ELSE 0 END)/COUNT(*),2) as 'Cancellation Rate'
FROM Trips
WHERE client_id IN (SELECT users_id FROM Users WHERE banned ='No')
AND
driver_id IN (SELECT users_id FROM USERS WHERE banned='No') and request_at BETWEEN "2013-10-01" and "2013-10-03"
GROUP BY request_at
