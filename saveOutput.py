class SaveSTT:
    def __init__(self, file, efolder='export'):
        self.file = file[:-4]   # Only file name not file extension
        self.efolder = efolder
        self.filepath = efolder + '/' + self.file + '.txt'
        self.__newfile()

    def __newfile(self):
        open(self.filepath, mode='w').close()

    def save(self, message):
        with open(self.filepath, 'a') as file:
            if message:
                file.write(message + ' ')