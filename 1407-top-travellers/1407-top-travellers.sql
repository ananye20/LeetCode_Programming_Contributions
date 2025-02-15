# Write your MySQL query statement below
SELECT name, IFNULL(SUM(distance),0) as travelled_distance
FROM Users U
LEFT JOIN Rides R
ON U.id = R.user_id
GROUP BY user_id
ORDER BY travelled_distance DESC, name