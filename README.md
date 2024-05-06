# Python GUI app with PostgreSQL Database

### Cloning the repo & Get to it
```shell
git clone https://github.com/h471x/python.git && cd python
```

### Install project libraries & Configuring PostgreSQL
```shell
python setup.py
```

### PostgreSQL User & Database Configuration

* Start the postgresql server on Linux
```shell
sudo systemctl start postgresql
```
* Start the postgresql server on WSL
```shell
sudo service postgresql start
```
* Load the postgresql database & user
```shell
sudo -u postgres psql -f config/postgres/python.sql 2>/dev/null
```
* Restart the postgresql service
```shell
sudo service postgresql restart
```
* Access the console with the new user
```shell
psql -U python -d python -h localhost -p 5432 -W
```
* python user password
```
python
```

### Launch the application

```shell
python main.py
```

### Resetting the application database

```shell
sudo -u postgres psql -f config/postgres/reset.sql 2>/dev/null
```
