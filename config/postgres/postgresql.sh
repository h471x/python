#!/bin/bash

# break a line
# echo -e
#
# # call sudo here first
# sudo echo "Backing Up postgreSQL configurations files..."
#
# # Find latest PostgreSQL version
pgVersion=$(ls -1 /etc/postgresql | grep '^[0-9]' | tail -n 1)
# pgPath="/etc/postgresql/$pgVersion/main"
#
# # Backup and copy new PostgreSQL configuration files
# pgConf="$pgPath/postgresql.conf"
# newConf="./config/postgres/postgresql.conf"
# if [ -f "$pgConf.bak" ]; then
# 	echo "postgresql.conf already configured."
# else
# 	echo -e
# 	echo "Enabling all IP to connect to the database..."
# 	sudo cp -rv "$pgConf" "$pgConf.bak" &&
# 		sudo cp -rv "$newConf" "$pgPath" || {
# 		echo "Failed to copy postgresql.conf"
# 		exit 1
# 	}
# fi
#
# # Backup and copy new pg_hba.conf file
# pgHba="$pgPath/pg_hba.conf"
# newHba="./config/postgres/pg_hba.conf"
# if [ -f "$pgHba.bak" ]; then
# 	echo "pg_hba.conf already configured."
# else
# 	echo -e
# 	echo "Allowing the user to access the database..."
# 	sudo cp -rv "$pgHba" "$pgHba.bak" &&
# 		sudo cp -rv "$newHba" "$pgPath" || {
# 		echo "Failed to copy pg_hba.conf"
# 		exit 1
# 	}
# fi
# echo "PostgreSQL configuration files updated successfully."
#
# # break a line
# echo -e
#
# # Check if running on WSL based on the existence of WSLInterop file
# isWSL="/proc/sys/fs/binfmt_misc/WSLInterop"
#
# # Check if any PostgreSQL processes are running
# if pgrep postgres >/dev/null; then
# 	echo "PostgreSQL server is already running"
# else
# 	echo "Starting the PostgreSQL server"
# 	[ -f "$isWSL" ] && sudo service postgresql start || sudo systemctl start postgresql
# fi

rawPgVersion=$(psql --version | awk '{print $3}')

# Convert the raw version to a number for comparison
pgVersionNumber=$(echo "$rawPgVersion" | awk -F. '{print $1*100 + $2}')

# Check if the PostgreSQL version is greater than 16.2
if [ "$pgVersionNumber" -gt 1602 ]; then
	# Fix the collation version mismatch
	# echo "Refreshing collation version for template1..."
	# sudo -u postgres psql -c "UPDATE pg_database SET datallowconn = TRUE WHERE datname = 'template1';"
	# sudo -u postgres psql -d template1 -c "VACUUM FULL;"
	# sudo -u postgres psql -d template1 -c "REINDEX DATABASE template1;"
	# sudo -u postgres psql -d template1 -c "ALTER DATABASE template1 REFRESH COLLATION VERSION;"
	# sudo -u postgres psql -c "UPDATE pg_database SET datallowconn = FALSE WHERE datname = 'template1';"
	#
	# # Create the python database if it does not exist
	# echo "Creating python database if it does not exist..."
	# sudo -u postgres psql -c "CREATE DATABASE python TEMPLATE template1;" || echo "Database python already exists."
	echo "pg versiion $pgVersion > 16.2"
else
	echo "pg version = $rawPgVersion <= 16.2"
fi
# Load the postgresql database configuration
# echo "Configuring PostgreSQL Database"
# sudo -u postgres psql -f config/postgres/reset.sql
# sudo -u postgres psql -f config/postgres/python.sql
