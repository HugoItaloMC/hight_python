import json

from xwrapper import Descritor

class RepoPost:
    def __init__(self):
        self.data = Descritor()
    
    def __iter__(self):
        self.__io = open('data.json', 'w+')
        self.__idx = 0
        return self
    
    def __next__(self):
        if self.__idx < len(self.data):
            self.__idx += 1

            if StopIteration:
                xdata = json.dumps({"data": self.data}, ensure_ascii=False)
                self.__io.write(xdata)
                self.__io.close()
        return self.__idx



class RepoGet:
    def __init__(self):
        self.data = Descritor()
    
    def __iter__(self):
        self.__io = open('data.json', 'r+')
        self.__idx = 0
        return self
    
    def __next__(self):
        if self.__idx < len(self.data):

            if StopIteration:
                xdata = json.loads(self.__io.read())
                data = xdata["data"]
                while _ := self.data.passwd == data[1] != True:
                    self.__idx += 1
                    return self.__idx, data
                    
                self.__io.close()
        return self.__idx
