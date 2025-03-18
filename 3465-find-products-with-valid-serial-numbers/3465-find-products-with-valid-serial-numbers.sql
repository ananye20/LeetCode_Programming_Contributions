# Write your MySQL query statement below
SELECT product_id, product_name, description
FROM products
WHERE description REGEXP 'SN[0-9]{4}-[0-9]{4}([^0-9]|$)'
ORDER BY product_id;
