from orm import create_session
from entities import User as UserModel
from wrapper import Descritor


class RepoUserPost:
    
    def __init__(self, *args):
        self.__args = args
    
    @property
    def args(self):
        return self.__args
    
    @args.setter
    def args(self, item):
        self.__args = item 
    
    
    def __coroutine(self):
        while True:
            yield
    
    def __next__(self, args):
        it = self.__coroutine()
        next(it)
        it.send(args)

    def __call__(self, method: str = None):
        db = create_session()

        # __call__ acessa dinâmicamente o dicionário da instância, podendo gerar atributos dinâmicos
        self.__post = Descritor()        
        if method:
            self.__post = self.args
            
            if method.upper() == 'POST':
                for line in self.__post:
                    name, passwd, email = line
                    user: UserModel = UserModel(name=name, passwd=passwd, email=email)
                self.__next__(db.add(user))
                self.__next__(db.commit())
        
        else:
            print('Insert Method from request')
        
    