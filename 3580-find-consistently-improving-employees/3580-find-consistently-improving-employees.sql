# Write your MySQL query statement below
WITH alll AS(SELECT E.employee_id AS emp_id, name, review_id, review_date, rating
FROM employees E
JOIN performance_reviews P
ON E.employee_id = P.employee_id),
ct_rws AS(SELECT name, COUNT(review_id) as count_of_rws
FROM alll
GROUP BY name),
modi AS(SELECT emp_id, A.name as name, review_id, review_date, rating, count_of_rws
FROM alll A
JOIN ct_rws C
ON A.name=C.name
WHERE count_of_rws>=3),
three AS(SELECT *, 
RANK() OVER (PARTITION BY emp_id ORDER BY review_date DESC) AS rnk
FROM modi),
final as(SELECT * FROM three 
WHERE rnk<=3),
semi_final as(SELECT *, COALESCE(LAG(rating) OVER (PARTITION BY emp_id ORDER BY review_date DESC),1000) as rate2 
FROM final),
final2 as(SELECT * 
FROM semi_final
WHERE rate2>rating),
grp as (SELECT emp_id, COUNT(rnk) as count_rank
FROM final2
GROUP BY emp_id
HAVING COUNT(rnk)=3),
final_g as(SELECT F.emp_id as employee_id, name, review_id, review_date, rating, rate2, count_rank
FROM final2 F
JOIN grp G
ON F.emp_id = G.emp_id)
SELECT employee_id, name, 
(MAX(rating)-MIN(rating)) AS improvement_score
FROM final_g
GROUP BY employee_id
HAVING (MAX(rating)-MIN(rating))>0
ORDER BY improvement_score DESC, name



