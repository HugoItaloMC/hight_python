from src.factory.core import Handler
from src.factory.tools.utils import PairNumber


class Abstract(Handler):

    def __init__(self, arg: set = {}, *args: tuple):
        super().__init__()
        self.__arg = arg
        self.__args = set(args)
    
    def __next__(self):
        if not self._exit and self.__arg:
            +self

            while self._exit > 0:
                -self
            
            if 'par' in self.__args:
                self.__args.discard('par')
                self.__arg = PairNumber(self.__arg)()

            xdata = self.__arg.pop()
            print(xdata)
        else:
            print("TAREFA `N` concluída")
            +self
            raise StopIteration
    

            

if __name__ == '__main__':
    ...