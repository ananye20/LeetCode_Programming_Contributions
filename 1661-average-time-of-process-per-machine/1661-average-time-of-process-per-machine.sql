# Write your MySQL query statement below
WITH starttable as (SELECT machine_id, process_id, SUM(timestamp) as st_time
FROM Activity
WHERE activity_type='start'
GROUP BY machine_id, process_id),

endtable as (SELECT machine_id, process_id, SUM(timestamp) as end_time
FROM Activity
WHERE activity_type='end'
GROUP BY machine_id, process_id)


SELECT S.machine_id, ROUND(((SUM(end_time) - SUM(st_time))/COUNT(DISTINCT S.process_id)),3) as processing_time
FROM starttable S
JOIN endtable E
ON S.machine_id = E.machine_id and S.process_id = E.process_id
GROUP BY S.machine_id


