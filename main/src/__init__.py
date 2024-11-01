from common import Common

class Facade:
    # chama sub-sistemas

    def __init__(self, data: set):
        self.__data = data
    
    def __iter__(self):
        op = yield
        common = iter(Common(op, self.__data))
        next(common)
        
        send = yield
        if 'SET' in send.upper():
            main = common.send('INIT')
            print(main.__dict__)
            main.attr = 'test'
            main.impar()
            yield (main.__dict__['_exit'], main.__dict__['_state'])
            main.run()
            print(main.__dict__)

        yield from self

if __name__ == '__main__':

    nfactory = iter(Facade(data=set(range(1, 101))))  # Enviando dados
    next(nfactory)  # Iniciando coroutina do objeto
    nfactory.send('N')  # BUSCANDO OPERACÃO
    print(nfactory.send('SET')) # Executando servico
    

    nfactory.send('N')
    

