from src.factory.core import AbstractPro as Handler

# Produtos Abstratos
# Produtos abstratos a qual vai conter regras a serem aplicadas, ou seja, ordens de servicos

class ConcretNN(Handler):

    def __init__(self, arg: set = {}):
        super().__init__()
        self.__arg = arg
    
    def __next__(self):
        if not self._exit and self.__arg:
            +self
            print("INICIANDO TAREFA `N`")
            while self._exit > 0:
                -self

            xdata = self.__arg.pop()
            print(xdata)
        else:
            print("TAREFA `N` concluída")
            +self
            raise StopIteration
            

if __name__ == '__main__':
    ...