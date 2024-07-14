from itertools import islice
from collections import namedtuple
from typing import Generator, Tuple, Coroutine, Any

from xrepository import RepoPost, RepoGet

class Schema:

    def __init__(self, data: Tuple):
        self.data = data
    
    def __iter__(self):
        Request: Tuple = namedtuple('Request', ('method', 'data'))
        methods: Tuple = ('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'TRACK')

        send: Coroutine = yield  # Após iniciar a coroutina com next() aguardando chamada de send()        

        if send in methods:  # Verificando primeiro send(METHOD)
            option: Generator = (data for data in Request(method=send, data=self.data))
            repo: Any[object[RepoGet | RepoPost]] = self.__xlogic(args=option)
            
            send: Coroutine = yield  # Aguardando próximo send()

            if 'SET' in send:  # Verificando argumento de send(SET)
                yield self.__xrequest(class_=repo)                
    
    
    def __xlogic(self, args: Generator):
        method = next(args)  # Recolhendo method

        truth = True if method in ['GET', 'POST'] else None
        
        if truth is not None:
            data = args.send(truth)  # Recolhendo dados
            
            if 'POST' in method:
                post = RepoPost()
                post.data = data
                return post
            
            elif 'GET' in method:
                get = RepoGet()
                get.data = data
                return get
    

    def __xrequest(self, class_):
        xiter = islice(class_, None)  # chamando __iter__ de class_
        idx = next(xiter)  # Chamando __next__() da class_
        return idx


if __name__ == '__main__':

    # RECEBENDO DADOS
    Data = namedtuple('Data', ('name', 'passwd', 'email'))
    #####

    schema = iter(Schema(data=Data('Hugo', 'passwd11', 'email')))  # Construindo objeto e chamando __init__ da instância
    try:
        next(schema)  # Iniciando Generator
        schema.send('GET')  # Chamando coroutina 1
        data = schema.send('SET')  # Chamando coroutina 2
        
        if isinstance(data, int):
            if not data:
                print('Not allowed')
        elif isinstance(data, tuple):
            if data[0]:
                print(data[1])
        
        next(schema)  # Chamando última coroutina
        

    except StopIteration:
        schema.close()




