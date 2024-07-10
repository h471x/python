SELECT s.student_id AS Matricule ,CONCAT(s.first_name,' ',s.last_name) AS Nom ,ce.cename AS UE ,g.theorical_grade AS Note ,CONCAT(t.first_name,' ',t.last_name) AS Enseignant
  FROM grade AS g 
  INNER JOIN student AS s
  ON g.fk_student_id=s.student_id
  INNER JOIN ce AS ce 
  ON g.fk_cename=ce.cename
  INNER JOIN teacher AS t 
  ON g.fk_teacher_id=t.teacher_id;


-- SELECT FOR STUDENT PAGE
SELECT s.student_id as Matricule,CONCAT(s.first_name,' ',s.last_name) AS Nom ,(g.theorical_grade + g.pratical_grade )/2 AS Note FROM grade AS g 
INNER JOIN student AS s
ON s.student_id=g.fk_student_id
WHERE s.level=value1 AND g.fk_cename=value2
ORDER BY s.student_id ASC;
