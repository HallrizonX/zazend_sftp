# ssh demo@test.rebex.net -p22
# password

from utils.Controller import Controller
from utils.DBManager import DBManager

if __name__ == "__main__":
    db = DBManager()
    id_connector = input('--->')
    db_arr = db.sql_get(id_connector)
    hostname = db_arr[1]
    password = db_arr[2]
    username = db_arr[3]

    cmd = Controller(hostname=hostname, password=password, username=username)
    cmd.run()
