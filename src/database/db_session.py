import arango
from arango import ArangoClient
from arango.database import StandardDatabase

__user = None


def global_init(db_file, database_name, username, password):
    global __user

    if __user:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать адрес базы данных.")

    client: arango.client.ArangoClient = ArangoClient(hosts=db_file)
    print(f"Подключение к базе данных по адресу {db_file}")

    __user = client.db(database_name, username=username, password=password)


def create_session() -> StandardDatabase:
    global __user
    return __user
