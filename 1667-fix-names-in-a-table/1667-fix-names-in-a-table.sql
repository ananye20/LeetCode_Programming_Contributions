-- Write your PostgreSQL query statement below
SELECT user_id, UPPER(LEFT(name, 1))||LOWER(SUBSTRING(name FROM 2)) as name
FROM Users
ORDER BY user_id;