#!/usr/bin/python

from config.database.connection.connect import (
    get_status, init_tables, load_sql_seed
)

from app.view.dashboard import dashboard_ui
from app.view.signin import signup_ui

if __name__ == '__main__':
    if get_status() == 'connected':
        if init_tables():
            # load_sql_seed()
            dashboard_ui()
            # signup_ui()
