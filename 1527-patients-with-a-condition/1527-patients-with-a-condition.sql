SELECT *
FROM Patients
WHERE conditions LIKE '%DIAB1%' 
  AND NOT conditions LIKE 'SADIAB%';
