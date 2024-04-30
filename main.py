from config.database.connect import connect
from app.view.gui import mainGui

if __name__ == '__main__':
    conn, status = connect()
    mainGui() if status == 'connected' else None
