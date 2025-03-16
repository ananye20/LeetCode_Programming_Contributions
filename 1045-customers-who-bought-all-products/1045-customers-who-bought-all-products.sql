WITH cte as (SELECT customer_id, COUNT(DISTINCT product_key) as ct
FROM Customer
GROUP BY customer_id)

SELECT customer_id
FROM cte
WHERE ct = (SELECT COUNT(product_key) FROM Product)