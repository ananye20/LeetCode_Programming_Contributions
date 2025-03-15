WITH tot AS (SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn ASC) as Total_Weight
FROM Queue
ORDER BY turn)

SELECT person_name FROM tot
WHERE Total_Weight<=1000
ORDER BY Total_Weight DESC
LIMIT 1
