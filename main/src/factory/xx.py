from src.factory.core import AbstractPro as Handler

class ConcretXX(Handler):

    def __init__(self, arg: set = {}):
        super().__init__()
        self.__arg = arg
    
    def __next__(self):
        if not self._exit and self.__arg:
            +self
            print("INICIANDO TAREFA `X`")
            while self._exit > 0:
                -self
            xdata = self.__arg.pop()
        else:
            print("TAREFA `X` concluída")
            +self
            raise StopIteration