from .ConnectionManager import ConnectionManager


class MoveManager(ConnectionManager):
    def move(self, folder: str = ""):
        if folder == "":
            folder: str = input("Enter your folder for move: ")
            folder = "{}{}/".format(self.state, folder)
            if self.srv.exists(folder):
                self.state = folder
        else:
            if self.srv.exists("{}{}/".format(self.state, folder)):
                self.state = "{}{}/".format(self.state, folder)

    def ls(self, show: bool = False):
        """Print list of all files, directories in current folder"""
        data = self.srv.listdir(self.state)
        if not show:
            return data
        else:
            for item in data:
                print(item)

    def back(self):
        state = "/".join(self.state.split('/')[:-2])
        if not state.endswith('/'):
            state += '/'
        self.state = state

    def pwd(self):
        print(self.state)
