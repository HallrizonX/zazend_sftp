from .FileManager import FileManager
from .MoveManager import MoveManager
from .Commander import Commander

class Controller(FileManager, MoveManager):

    def run(self):
        while True:
            command = input("{}^: ".format(self.state)).strip()

            # Start Move manager
            if command == 'back':
                self.back()
            if 'cd' in command:
                if len(command) > 2:
                    self.move(folder=command.split(' ')[-1])
                else:
                    self.move()
            if command == 'ls':
                self.ls(show=True)
            if command == 'pwd':
                self.pwd()
            # End move manager

            if command == 'help':
                Commander.help()

            # Start File manager
            if command == 'd':
                self.download()

            if command == 'upload':
                self.upload()

            if command == 'r':
                self.read()
            # End File manager

            if command == 'q' or command == 'quit':
                self.srv.close()
                break
