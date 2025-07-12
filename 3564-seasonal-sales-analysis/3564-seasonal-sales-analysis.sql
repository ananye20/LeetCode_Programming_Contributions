# Write your MySQL query statement below
WITH cte AS(SELECT S.product_id as product_id, category, quantity, product_name, sale_date, price, sale_id,(quantity*price) AS revenue,
CASE WHEN MONTH(sale_date) IN (12,1,2) THEN "Winter"
WHEN MONTH(sale_date) IN (3,4,5) THEN "Spring"
WHEN MONTH(sale_date) IN (6,7,8) THEN "Summer"
WHEN MONTH(sale_date) IN (9,10,11) THEN "Fall"
END AS season
FROM sales S
JOIN products P
ON S.product_id = P.product_id),
cse AS (SELECT season, category, SUM(quantity) AS total_quantity, SUM(revenue) AS total_revenue
FROM cte
GROUP BY season, category),
abc AS(SELECT season, category, total_quantity, total_revenue, RANK() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS rnk
FROM cse)
SELECT season, category, total_quantity, total_revenue
FROM abc
WHERE rnk=1
