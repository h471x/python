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
pgVersion=$(ls -1 /etc/postgresql | grep '^[0-9]' | tail -n 1)
pgPath=/etc/postgresql/$pgVersion/main
pgConf=$pgPath/postgresql.conf
newConf=config/postgres/postgresql.conf
sudo cp -rv $pgConf $pgConf.bak
sudo cp -rv $newConf $pgPath
```

### Allowing the user to access the database

```shell
pgVersion=$(ls -1 /etc/postgresql | grep '^[0-9]' | tail -n 1)
pgPath=/etc/postgresql/$pgVersion/main
pgGba=$pgPath/pg_gba.conf
newGba=config/postgres/pg_gba.conf
sudo cp -rv $pgGba $pgGba.bak
sudo cp -rv $newGba $pgPath
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
