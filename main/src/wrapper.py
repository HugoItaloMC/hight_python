from collections import namedtuple
from queue import Queue   

from src.factory import Factory
__all__ = ['Common']

class Wrapper:
    # Acesso a `Factorys, fabricas `
    # Neste Objeto vc escolhe através de atributos como utilizar a factory
    def __init__(self, op: str, data: set, *args: tuple):
        self.__op = op  # Operacão contida nas tarefas enviadas do FrontEnd
        self.__data = data  # Dados
        self.__args = args  # Envia funcões auxiliares para Factory
        self._queue = Queue()

 
    def __iter__(self):
        # Estruturando requisicão
        Request = namedtuple('Request', ("op", "data"))
        
        send = yield
        if 'INIT' in send.upper():
            yield self.__logic((x for x in Request(op=self.__op, data=self.__data)))
        yield from self.__dict__

    
    def __logic(self, generator):
        OPERATIONS = ('N')
        op = next(generator)

        if self.__args and op:
            self._queue.put(Factory(next(generator), self.__args[0]))

        elif op in OPERATIONS:
            self._queue.put(Factory(next(generator)))

        else:
            generator.close()
            exit()
            
        generator.close()
        yield self._queue
    

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