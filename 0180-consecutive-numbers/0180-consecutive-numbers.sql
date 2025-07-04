WITH lags AS(SELECT id, num, LAG(num) OVER (ORDER BY id) AS lag_num1
FROM Logs),
lags2 AS(SELECT *, LAG(lag_num1) OVER (ORDER BY id) AS lag_num2
FROM lags)
SELECT DISTINCT num AS ConsecutiveNums FROM lags2
WHERE num=lag_num1 AND lag_num1=lag_num2