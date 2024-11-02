from src.common import Common
__all__ = ['Facade']

class Facade:
    # chama Common passando qual factory utilizar

    def __init__(self, data: set):
        self.__data = data
    
    def __iter__(self):
        op = yield  # Recebe qual Factory utilizar através de corroutina
        common = iter(Common(op, self.__data))  # Trazendo factory para chamada de pilha com a instância de `Common`
        next(common)  # Iniciando a corroutina de `Common`
        
        # Contrato externo para iniciar tarefas na factory atual  
        send = yield  
        if 'SET' in send.upper():
            recv = common.send('INIT')  # Referênciando Factory a mesma se encontra em uma  `Queue` como um generator
            queue = next(recv)  # recolhendo `Queue` do generator
            main = queue.get()  # buscando Factory contida na `Queue`
            #print(main.__dict__)
            #main.attr = 'test'  # Adiministrando novos atributos para a factory
            #main.impar()  # Tarefa de alto nível, ñ altera o estado e saída da classe concreta da Factory
            yield main.run()  # Enviando o estado e saída da Factory através de corroutina
        yield from self

if __name__ == '__main__':

    task = iter(Facade(data=set(range(0, 101))))  # Enviando dados
    next(task)  # Iniciando coroutina do objeto
    task.send('N')  # BUSCANDO OPERACÃO
    task.send('SET') # Executando servico
    
    

