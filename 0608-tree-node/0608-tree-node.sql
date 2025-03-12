# Write your MySQL query statement below
SELECT id, (CASE WHEN p_id is null THEN 'Root' WHEN id IN (SELECT p_id FROM Tree)
THEN 'Inner'
WHEN id NOT IN (SELECT p_id FROM Tree) OR p_id IS NOT null
THEN 'Leaf' END) as type
FROM Tree
GROUP BY id
