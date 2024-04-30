# Python GUI app with PostgreSQL Database

### Setup the project
```shell
python setup.py
```
### Enabling all IP to connect to the database

```shell
sudoedit /etc/postgresql/*/main/postgresql.conf
```

* Inside this file edit the line like so
```
listen_addresses = '*'
```

### Allowing the user to access the database

```shell
sudoedit /etc/postgresql/*/main/pg_gba.conf
```

* Inside this file edit the line like so
```
# TYPE  DATABASE        USER            ADDRESS                 METHOD
host    all             all             0.0.0.0/0               md5
```


### PostgreSQL User Creation

* Start the postgresql server
```shell
sudo service postgresql start
```
* Switch to the postgresql user
```shell
sudo su - postgres
```
* Access the shell of postgresql
```shell
psql
```
* New user with permissions
```psql
CREATE USER python WITH PASSWORD 'python';
GRANT ALL PRIVILEGES ON DATABASE postgres TO python;
```
* Exit the shell
```psql
\q
```
* Exit the postgres user session
```shell
exit
```
* Restart the postgresql service
```shell
sudo service postgresql restart
```
