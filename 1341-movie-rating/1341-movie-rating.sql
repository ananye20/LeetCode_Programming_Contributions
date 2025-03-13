
SELECT results FROM (
    SELECT U.name AS results
    FROM Users U
    JOIN MovieRating MR ON U.user_id = MR.user_id
    GROUP BY U.user_id, U.name
    ORDER BY COUNT(MR.movie_id) DESC, U.name ASC
    LIMIT 1
) AS user_ranking

UNION ALL

SELECT results FROM (
    SELECT M.title AS results
    FROM Movies M
    JOIN MovieRating MR ON M.movie_id = MR.movie_id
    WHERE YEAR(MR.created_at) = 2020 AND MONTH(MR.created_at) = 2
    GROUP BY M.movie_id, M.title
    ORDER BY AVG(MR.rating) DESC, M.title ASC
    LIMIT 1
) AS movie_ranking;
