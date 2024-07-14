import json
from secrets import token_hex

class RepoPost:
    def __init__(self, **kw: dict):
        self.kw = kw
    
    def __iter__(self):
        self.__io = open('schema.json', 'w+')
        self.__idx = 0
        return self
    
    def __next__(self):
        if self.__idx < len(self.kw.items()):
            data = {}

            for key, valur in self.kw.items():
                data[key] = valur
                self.__idx += 1

            if StopIteration:
                xdata = json.dumps(data)
                self.__io.write(xdata)
                self.__io.close()


class RepoGet:
    def __init__(self, **kw: dict):
        self.kw = kw
    
    def __iter__(self):
        self.__io = open('schema.json', 'r+')
        return self
    
    def __next__(self):
        xjson = json.loads(self.__io.read())
        if xjson['passwd'] == self.kw['passwd']:
            self.token = token_hex(16)  # Gerando token após `login` confirmado
        else:
            print('Incorrect Password')
        return self


class RepoPut:
    def __init__(self, **kw: dict):
        self.kw = kw
    
    def __iter__(self):
        self.__io = open('schema.json', 'w+')
        self.__idx = 0
        return self
    
    def __next__(self):
        if self.__idx < len(self.kw.items()):
            data = {}

            for key, valur in self.kw.items():
                data[key] = valur
                self.__idx += 1

            if StopIteration:
                xdata = json.dumps(data)
                self.__io.write(xdata)
                self.__io.close()

