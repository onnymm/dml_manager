import os

class _Env():
    _host = 'DB_HOST'
    _port = 'DB_PORT'
    _db_name = 'DB_NAME'
    _user = 'DB_USER'
    _password = 'DB_PASSWORD'

    def __init__(self) -> None:
        self._credentials = {}
        self._credentials['host'] = os.environ.get(self._host)
        self._credentials['port'] = os.environ.get(self._port)
        self._credentials['db_name'] = os.environ.get(self._db_name)
        self._credentials['user'] = os.environ.get(self._user)
        self._credentials['password'] = os.environ.get(self._password)
