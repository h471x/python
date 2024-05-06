#!/bin/bash

# break a line
echo -e

# call sudo here first
sudo echo "Backing Up postgreSQL configurations files..."

# Find latest PostgreSQL version
pgVersion=$(ls -1 /etc/postgresql | grep '^[0-9]' | tail -n 1)
pgPath="/etc/postgresql/$pgVersion/main"

# Backup and copy new PostgreSQL configuration files
pgConf="$pgPath/postgresql.conf"
newConf="./config/postgres/postgresql.conf"
if [ -f "$pgConf.bak" ]; then
	echo "postgresql.conf already configured."
else
	echo -e
	echo "Enabling all IP to connect to the database..."
	sudo cp -rv "$pgConf" "$pgConf.bak" &&
		sudo cp -rv "$newConf" "$pgPath" || {
		echo "Failed to copy postgresql.conf"
		exit 1
	}
fi

# Backup and copy new pg_hba.conf file
pgHba="$pgPath/pg_hba.conf"
newHba="./config/postgres/pg_hba.conf"
if [ -f "$pgHba.bak" ]; then
	echo "pg_hba.conf already configured."
else
	echo -e
	echo "Allowing the user to access the database..."
	sudo cp -rv "$pgHba" "$pgHba.bak" &&
		sudo cp -rv "$newHba" "$pgPath" || {
		echo "Failed to copy pg_hba.conf"
		exit 1
	}
fi

echo -e
echo "PostgreSQL configuration files updated successfully."

# break a line
echo -e
