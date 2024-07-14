from orm import create_session
from entities import User as UserModel


class RepoUser:
    
    def __init__(self, *args):
        self.args = args
    
    def coroutine(self):
        while True:
            yield
    
    def __next__(self, args):
        it = self.coroutine()
        next(it)
        it.send(args)
    
    
    def __call__(self):
        db = create_session()
        print(self.args)

    