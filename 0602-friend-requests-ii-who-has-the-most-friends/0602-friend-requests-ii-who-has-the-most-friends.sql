SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) combined
GROUP BY id
HAVING num = (
    SELECT MAX(num_count) 
    FROM (
        SELECT id, COUNT(*) AS num_count
        FROM (
            SELECT requester_id AS id FROM RequestAccepted
            UNION ALL
            SELECT accepter_id AS id FROM RequestAccepted
        ) inner_combined
        GROUP BY id
    ) max_table
);
