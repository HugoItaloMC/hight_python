from collections import namedtuple
from queue import Queue   

from factory import(FactoryNN, FactoryXX, ConcretYY)
__all__ = ['Common']

class Common:
    # Abstract Factory
    # Acesso a `Factorys, fabricas `
    # Neste Objeto vc escolhe através de condicões qual Produto conreto utilizar
    def __init__(self, op: str, data: set):
        self.__op = op
        self.__data = data
        self._queue = Queue()
    
    def __iter__(self):
        Request = namedtuple('Request', ("op", "data"))
        
        send = yield
        if 'INIT' in send.upper():
            grequest = (x for x in Request(op=self.__op, data=self.__data))
            yield self.__logic(grequest)
        yield from self

    
    def __logic(self, generator):
        OPERATIONS = ('N', 'Y', 'X')
        op = next(generator)
        if 'N' in op:
            self._queue.put(FactoryNN(next(generator)))
        elif 'Y' in op:
            self._queue.put(FactoryYY(next(generator)))
        elif 'X' in op:
            self._queue.put(FactoryXX(next(generator)))
        else:
            generator.close()
            print("operation error")
            exit(0)
            
        generator.close()
        return self._queue.get()
    

if __name__ == '__main__':
    xdata = set(range(1, 101))
    xmain = iter(Main('X', xdata))
    next(xmain)
    xservice = xmain.send('INIT')

    print(xservice.__dict__, '\n%s'% id(xservice))
    xservice.run()
    print(xservice.__dict__, '\n%s'% id(xservice))
    xmain.close()

    
    ydata = set(range(1, 101))
    ymain = iter(Main('Y', ydata))
    next(ymain)
    yservice = ymain.send('INIT')

    print(yservice.__dict__, '\n%s'% id(yservice))
    yservice.run()
    print(yservice.__dict__, '\n%s'% id(yservice))
    ymain.close()
        
    ndata = set(range(1, 101))
    nmain = iter(Main('N', ndata))
    next(nmain)
    nservice = nmain.send('INIT')

    print(nservice.__dict__, '\n%s'% id(nservice))
    nservice.run()
    print(nservice.__dict__, '\n%s'% id(nservice))
    nmain.close()

    #  ERROR
    edata = set(range(1, 101))
    emain = iter(Main('E', ndata))
    next(emain)
    
    eservice = emain.send('INIT')
    print(emain)

    print(eservice.__dict__, '\n%s'% id(eservice))
    eservice.run()
    print(nservice.__dict__, '\n%s'% id(eservice))
    emain.close()