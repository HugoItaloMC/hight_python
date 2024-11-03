from src.factory.core import AbstractAlfa as Handler
from src.factory.tools.utils import Utils

"""
    - Classe concreta, nesta classe temos
    que tem uma tarefa principal, e chama
    outras instâncias de sub-classes de 
    `Handler` para poder manipular `arg` 
    diretamente.

"""

class Concret(Handler):

    def __init__(self, arg: set = {}, *args: tuple):
        super().__init__()
        self.__arg = arg
        self.__args = set(args)
    
    def __next__(self):
        if not self._exit and self.__arg:
            +self

            while self._exit > 0:
                -self
            
            if 'utils' in self.__args:
                self.__args.pop()
                Utils('data')()

            xdata = self.__arg.pop()
            print(xdata)
        else:
            print("TAREFA `N` concluída")
            +self
            raise StopIteration
    

            

if __name__ == '__main__':
    ...