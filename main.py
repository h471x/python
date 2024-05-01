from config.database.connect import getStatus
from app.view.gui import mainGui

if __name__ == '__main__':
    mainGui() if getStatus() == 'connected' else None
