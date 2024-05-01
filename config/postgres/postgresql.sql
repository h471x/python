DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_catalog.pg_user WHERE usename = 'python'
    ) THEN
    CREATE USER python WITH PASSWORD 'python';
    GRANT ALL PRIVILEGES ON SCHEMA public TO python;
  END IF;

  IF NOT EXISTS (
    SELECT 1 FROM pg_database WHERE datname = 'python'
  ) THEN
    CREATE DATABASE python;
    ALTER DATABASE python OWNER TO python;
    GRANT ALL PRIVILEGES ON DATABASE python TO python;
  END IF;
END $$;
