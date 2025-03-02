# Write your MySQL query statement below
SELECT s.name as name
FROM salesperson s
LEFT JOIN orders o
using(sales_id)
LEFT JOIN company c
using(com_id)
GROUP BY s.sales_id
HAVING sum(c.name = 'RED') = 0 or sum(c.name is null) > 0