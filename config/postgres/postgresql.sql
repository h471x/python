DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_database WHERE datname = 'python'
  ) THEN
    CREATE DATABASE python;
  END IF;

  IF NOT EXISTS (
    SELECT 1 FROM pg_catalog.pg_user WHERE usename = 'python'
  ) THEN
    CREATE USER python WITH PASSWORD 'python';
  END IF;
END $$;
GRANT ALL PRIVILEGES ON DATABASE python TO python;
GRANT ALL PRIVILEGES ON SCHEMA public TO python;
