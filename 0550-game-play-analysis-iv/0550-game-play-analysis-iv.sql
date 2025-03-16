WITH FirstLogin AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT 
    ROUND(
        COUNT(DISTINCT A.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2
    ) AS fraction
FROM Activity A
JOIN FirstLogin F
ON A.player_id = F.player_id
WHERE A.event_date = F.first_login + INTERVAL 1 DAY;
