# Python GUI app with PostgreSQL Database

### Cloning the repo & Get to it
```shell
git clone https://github.com/h471x/python.git && cd python
```

### Install project libraries
```shell
python setup.py
```

### Enabling all IP to connect to the database

```shell
pgConf=/etc/postgresql/*/main/postgresql.conf
newConf=config/postgres/postgresql.conf
sudo mv $pgConf $pgConf.bak
sudo cat $newConf > $pgConf
```

### Allowing the user to access the database

```shell
pgGba=/etc/postgresql/*/main/pg_gba.conf
newGba=config/postgres/pg_gba.conf
sudo mv $pgGba $pgGba.bak
sudo cat $newGba > $pgGba
```

### PostgreSQL User & Database Configuration

* Start the postgresql server
```shell
sudo service postgresql start
```
* Load the postgresql database & user
```shell
sudo -u postgres psql -f config/postgres/postgresql.sql &>/dev/null
```
* Restart the postgresql service
```shell
sudo service postgresql restart
```
* Access the console with the new user
```shell
psql -U python -d python -W
```
* python user password
```
python
```

### Launch the application

```shell
python main.py
```
