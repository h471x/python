## Manual database configurations

* Init the database
```shell
sudo -u postgres psql -f config/postgres/python/python.sql 2>/dev/null
```
* Reset database
```shell
sudo -u postgres psql -f config/postgres/python/reset.sql 2>/dev/null
```
* Access the console with the python user
```shell
psql -U python -d python -h localhost -p 5432 -W
```
* python user password
```
python
```
