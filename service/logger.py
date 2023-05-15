import datetime

class LoggerService:
    def __init__(self,filename,debug:bool):
        self.filename = filename
        self.debug = debug
        self.file = open(filename,'a')
        self.file.close()

    def getDate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def log(self,message):
        line = f"[{self.getDate()}] [INFO] : {message}"
        print(line)
        self.file = open(self.filename,'a')
        self.file.write(line+'\n')
        self.file.close()

    def error(self,message):
        line = f"[{self.getDate()}] [ERROR] : {message}"
        print(line)
        self.file = open(self.filename,'a')
        self.file.write(line+'\n')
        self.file.close()

    def warning(self,message):
        line = f"[{self.getDate()}] [WARNING] : {message}"
        print(line)
        self.file = open(self.filename,'a')
        self.file.write(line+'\n')
        self.file.close()

    def debug(self,message):
        line = f"[{self.getDate()}] [DEBUG] : {message}"
        if self.debug:
            print(line)
        self.file = open(self.filename,'a')
        self.file.write(line+'\n')
        self.file.close()
