from pysftp import Connection


class ConnectionManager:
    state: str = ""
    svr: str = ""

    def __init__(self,
                 hostname: str = "test.rebex.net",
                 username: str = "demo",
                 password: str = "password"
                 ):
        self.srv = Connection(host=hostname, username=username, password=password)
        self.state = self.srv.pwd

    def __del__(self):
        self.srv.close()
