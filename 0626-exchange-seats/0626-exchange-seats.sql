SELECT id, 
COALESCE(CASE WHEN id%2!=0 THEN LEAD(student) OVER (ORDER BY id)
WHEN id%2=0 THEN LAG(student) OVER (ORDER BY id) END, student)
as student
FROM Seat