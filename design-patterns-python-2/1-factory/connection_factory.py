class MySQLdb:
    def __init__(self) -> None:
        self._host: str
        self._user: str
        self._passwd: str
        self._db: str

    def connect(self, host: str, user: str, passwd: str, db: str) -> None:
        self._host = host
        self._user = user
        self._passwd = passwd
        self._db = db
        print(f"MySQLdb HOST:{host},  USER:{user}, PASSWORD:{passwd}, DATABASE:{db}")


class ConnectionFactory:
    def get_connection(self) -> None:
        return MySQLdb().connect(host="localhost", user="root", passwd="", db="teste_factory")
