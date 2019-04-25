class Commander:
    @staticmethod
    def help():
        str_ls: str = "\nls - Print list of all files, directories in current folder"
        str_download: str = "\ndownload/d - Download file from server by file name"
        str_help: str = "\nhelp - Print list of all commands"
        str_read: str = "\nread/r - Reading file from server"
        print(str_help,
              str_ls,
              str_download,
              str_read
              + '\n')
