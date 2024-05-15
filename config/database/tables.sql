CREATE TABLE person(
  id_card TEXT PRIMARY KEY,
  last_name TEXT NOT NULL,
  first_name TEXT,
  birth DATE NOT NULL,
  gender VARCHAR(1) NOT NULL CHECK( Gender IN('M','F')),
  adress TEXT NOT NULL,
  phone VARCHAR(10) NOT NULL
);
CREATE TABLE admin(
  username TEXT PRIMARY KEY ,
  password TEXT NOT NULL
) INHERITS (person);
CREATE TABLE student(
  id TEXT PRIMARY KEY,
  major TEXT NOT NULL,
  Grade TEXT NOT NULL,
  cursus TEXT NOT NULL
) INHERITS (person);
CREATE TABLE teacher(
  
) INHERITS (person);
CREATE TABLE ce(
  cename TEXT PRIMARY KEY,
  ue TEXT NOT NULL
);
CREATE TABLE grade(
  gradeId SERIAL PRIMARY KEY,
  theorical_grade INT NOT NULL DEFAULT 20,
  pratical_grade INT NOT NULL DEFAULT 20
);
