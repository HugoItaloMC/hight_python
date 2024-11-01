from src.factory.nn import ConcretNN
from src.factory.xx import ConcretXX
from src.factory.yy import ConcretYY
__all__ = ['FactoryXX', 'FactoryYY', 'FactoryNN']


# Factorys 
# Faz uma refrência a produtos concretos


class FactoryNN(ConcretNN): 
    run: 'Handler' = ...
    def __init__(self, arg, *args, **kw):
        super().__init__(arg)
        self.__args = args
        self.__kw = kw
    
    def __getattr__(self, attr):
        valur = attr
        setattr(valur, self, attr)
        return valur

    def impar(self):
        self._ConcretNN__arg = {x for x in self._ConcretNN__arg if x % 2 != 0}



class FactoryXX(ConcretXX): 
    run: 'Handler' = ...

class FactoryYY(ConcretYY): 
    run: 'Handler' = ...

if __name__ == '__main__':
    nn = ConcretN(set(range(1, 101)))
    nn.run()