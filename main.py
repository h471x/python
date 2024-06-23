#!/usr/bin/python

from config.database.connection.connect import get_status, init_tables

from app.view.dashboard import dashboard_ui

if __name__ == '__main__':
    if get_status() == 'connected':
        if init_tables():
            dashboard_ui()
