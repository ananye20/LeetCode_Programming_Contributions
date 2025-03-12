SELECT u.user_id AS buyer_id, u.join_date, 
COALESCE(COUNT(o.order_id), 0) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o 
ON u.user_id = o.buyer_id 
AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date;
