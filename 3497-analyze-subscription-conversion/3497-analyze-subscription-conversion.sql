# Write your MySQL query statement below
WITH cte AS (SELECT user_id, activity_type,
CASE WHEN activity_type='free_trial' THEN SUM(activity_duration)/COUNT(user_id)
WHEN activity_type='paid' THEN SUM(activity_duration)/COUNT(user_id) 
WHEN activity_type='cancelled' THEN SUM(activity_duration) END as tra
FROM UserActivity
WHERE user_id IN (SELECT user_id FROM UserActivity
WHERE activity_type='paid')
GROUP BY user_id, activity_type)

SELECT user_id,
ROUND(MAX(CASE WHEN activity_type='free_trial' THEN tra END),2) as trial_avg_duration,
ROUND(MAX(CASE WHEN activity_type='paid' THEN tra END),2) as paid_avg_duration
FROM cte
GROUP BY user_id
