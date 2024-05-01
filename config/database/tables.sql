CREATE TABLE IF NOT EXISTS APP_USER (
  username TEXT NOT NULL UNIQUE,
  lastname TEXT NOT NULL,
  firstname TEXT,
  user_address TEXT NOT NULL,
  contact_info TEXT NOT NULL,
  PRIMARY KEY(username)
);
