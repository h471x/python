CREATE TABLE IF NOT EXISTS person(
  id_card TEXT PRIMARY KEY,
  last_name TEXT NOT NULL,
  first_name TEXT,
  birth DATE NOT NULL,
  gender VARCHAR(1) NOT NULL CHECK( Gender IN('M','F')),
  adress TEXT NOT NULL,
  phone VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS admin(
  username TEXT PRIMARY KEY ,
  password TEXT NOT NULL,
  workstation TEXT NOT NULL
) INHERITS (person);

CREATE TABLE IF NOT EXISTS student(
  student_id TEXT PRIMARY KEY,
  major TEXT NOT NULL,
  level TEXT NOT NULL,
  cursus TEXT NOT NULL
) INHERITS (person);

CREATE TABLE IF NOT EXISTS teacher(
  teacher_id TEXT PRIMARY KEY
  
) INHERITS (person);

CREATE TABLE IF NOT EXISTS ce(
  cename TEXT PRIMARY KEY,
  ue TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS grade(
  theorical_grade INT NOT NULL DEFAULT 20,
  pratical_grade INT NOT NULL DEFAULT 20,
  fk_cename TEXT NOT NULL,
  fk_student_id TEXT NOT NULL,
  fk_teacher_id TEXT NOT NULL,
  FOREIGN KEY(fk_student_id) REFERENCES student(student_id),
  FOREIGN KEY(fk_cename) REFERENCES ce(cename),
  FOREIGN KEY(fk_teacher_id) REFERENCES teacher(teacher_id),
  PRIMARY KEY(fk_cename,fk_teacher_id,fk_student_id)
);


--OLD VERSION

-- CREATE TABLE IF NOT EXISTS grade(
--   gradeId SERIAL PRIMARY KEY,
--   theorical_grade INT NOT NULL DEFAULT 20,
--   pratical_grade INT NOT NULL DEFAULT 20,
--   fk_cename TEXT NOT NULL,
--   FOREIGN KEY(fk_cename) REFERENCES ce(cename)
-- );

--RELATION TABLE

-- CREATE TABLE IF NOT EXISTS have (
--   rf_id TEXT ,
--   rf_cename TEXT,
--   PRIMARY KEY(rf_id,rf_cename),
--   FOREIGN KEY(rf_id) REFERENCES student(id),
--   FOREIGN KEY(rf_cename) REFERENCES ce(cename)
-- );
