INSERT INTO student (
  id_card,
  first_name,
  last_name,
  birth,
  gender,
  adress,
  phone,
  student_id,
  major,
  level,
  cursus
) VALUES ( 
  '0123456789',
  'Marc',
  'Parker',
  '2003-05-22',
  'M',
  'New York',
  '0123456789',
  '0006',
  'Computer science',
  'M2',
  'Cyber security'
  );

INSERT INTO teacher (
  id_card,
  first_name,
  last_name,
  birth,
  gender,
  adress,
  phone,
  teacher_id
) VALUES (
  '0123456789',
  'RAKOTONDRANAIVO',
  'Paul',
  '1989-02-10',
  'M',
  'Califorinia',
  '12345678',
  '34B'
  );
INSERT INTO ce (
  cename,
  ue
) VALUES ( 
  'Electronique Analogique',
  'Electronique'
  );
INSERT INTO grade(
  theorical_grade ,
  fk_cename,
  fk_student_id,
  fk_teacher_id
) VALUES (
  11,
  'Electronique Analogique',
  '0006',
  '34B'
  )
