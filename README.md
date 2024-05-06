# Python GUI app with PostgreSQL Database

### Cloning the repo & Get to it
```shell
git clone https://github.com/h471x/python.git && cd python
```

### Install project libraries & Configuring PostgreSQL
```shell
python setup.py
```

### Launch the application

```shell
python main.py
```

### Manual database configurations

* Reset database
```shell
sudo -u postgres psql -f config/postgres/reset.sql 2>/dev/null
```
* Access the console with the new user
```shell
psql -U python -d python -h localhost -p 5432 -W
```
* python user password
```
python
```
