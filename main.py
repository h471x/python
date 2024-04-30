from config.database.connect import connect
from app.view.gui import mainGui

if __name__ == '__main__':
    conn, status = connect()

    if status == 'disconnected':
        print('Not connected to the PostgreSQL Database.')
    elif status == 'connected':
        mainGui()
