# Write your MySQL query statement below
SELECT product_name, SUM(unit) as unit
FROM Products P
JOIN Orders O
ON P.product_id = O.product_id
WHERE order_date like "2020-02-__"
GROUP BY product_name
HAVING SUM(unit)>=100

