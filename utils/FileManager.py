from .ConnectionManager import ConnectionManager


class FileManager(ConnectionManager):
    def upload(self):
        """Upload file to server"""
        filename: str = input("Enter your file name for upload to server: ")
        self.srv.put(filename)

    def download(self):
        """Download file from server"""
        filename: str = input("Enter file name: ")
        filename = "{}{}".format(self.state, filename)
        if self.srv.exists(filename):
            try:
                file = self.srv.get(filename)
                print("File {} was success download".format(filename))
            except TypeError:
                print("File {} is success download but it's empty".format(filename))

    def read(self):
        """Read file into console"""
        filename: str = input("Enter file name for reading: ")
        filename = "{}{}".format(self.state, filename)
        if self.srv.exists(filename):
            file = self.srv.get(filename)
            print(file)
