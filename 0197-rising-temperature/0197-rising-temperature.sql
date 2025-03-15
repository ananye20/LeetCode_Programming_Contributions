WITH abc as(SELECT id, recordDate, temperature, LAG(temperature) OVER (ORDER BY recordDate) as newtemp
FROM Weather
)

SELECT id
FROM abc
WHERE temperature>newtemp AND newtemp IS NOT NULL
and recordDate - INTERVAL 1 DAY IN (SELECT recordDate FROM Weather)