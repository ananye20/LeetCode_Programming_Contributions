WITH userct as (SELECT name as results
FROM Users U
RIGHT JOIN MovieRating MR
ON U.user_id = MR.user_id
GROUP BY name
HAVING COUNT(MR.user_id)>0
ORDER BY COUNT(MR.user_id) DESC, name ASC
LIMIT 1),

mvename as (SELECT title as results
FROM MovieRating MR
LEFT JOIN Movies M
ON MR.movie_id = M.movie_id
WHERE YEAR(created_at)='2020' AND MONTH(created_at)='02'
GROUP BY title
HAVING AVG(rating)>0
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1)

SELECT * FROM userct
UNION ALL
SELECT * FROM mvename