SELECT S.student_id, student_name, SU.subject_name, COUNT(E.student_id) as attended_exams
FROM Students S
CROSS JOIN Subjects SU
LEFT JOIN Examinations E
ON S.student_id = E.student_id AND E.subject_name = SU.subject_name
GROUP BY S.student_id, student_name, SU.subject_name
ORDER BY S.student_id
