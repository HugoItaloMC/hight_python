import json
from typing import Generator, Tuple
from collections import namedtuple
from itertools import islice, starmap

from wrapper import Descritor


Data= namedtuple('Data', ('name', 'passwd', 'email'))
Request = namedtuple('Request', ('method', 'data'))


class RepoPost:
    def __init__(self):
        self.data = Descritor()
    
    def __iter__(self):
        self.__io = open('data.json', 'w+')
        self.__idx = 0
        return self
    
    def __next__(self):
        if self.__idx < len(self.data):
            self.__idx += 1

            if StopIteration:
                xdata = json.dumps({"data": self.data}, ensure_ascii=False)
                self.__io.write(xdata)
                self.__io.close()
        return self.__idx



def xrequest(class_: Generator):
    """
      - Envia a requisicão para armazenar ou recuperar os dados

      params:
        class_: Uma classe representando repository e uma entidade
    """
    xiter = islice(class_, None)  # Chamando __iter__() de class_
    idx = next(xiter)  # chamando __next__() de class_
    return idx
    


def xsteps(data: Tuple):
    """
      - Delega a lógica (xlogic) e a requisicão(xrequest), recebe os dados
      e qual parâmetro utilizar

      return:
       None

      params:
        args: Tuple

    """
    methods = ('POST', 'GET', 'PUT', 'DELETE')    
    
    send = yield  # Inicia após a chamada de next()
    
    if send in methods:  # Verificando contrato externo, chamada do método send(bool)

        request: list = [(option for option in Request(method=send, data=data))]
        xrepo = starmap(xlogic, [request])
        
        send = yield #  Verificando novamento o send(bool)
        if 'SET' in send: # contrato externo
            for repo in xrepo:
                yield xrequest(class_=repo)


def xlogic(args: Generator):
    """
      - Aplica regras condicionais para 
      evolucão da aplicacão
    """
    methods = ['GET', 'PUT', 'DELETE', 'POST']
    method = next(args)  # Iniciando generator, recolhendo primeiro argumento 'method'
    
    truth = True if method in methods else None
    
    if truth is not None:
        if 'POST' in method:
            data = args.send(truth)  # Recolhendo segundo argumento 'data'
            
            repo = RepoPost()
            repo.data = data
            
            return repo 


def main():

    # ESTRUTURA DE DADOS
    data = Data(name='Hugo', passwd='passwd', email='email')
    #######
    
    try:
        it = xsteps(data)
        next(it)  # Iniciando Generator
        it.send('POST')  # Enviando sinal para xlogic(args)
        
        # Enviando o sinal para xrequest(class_)
        it.send('SET')  
        next(it)  # chamando coroutina referenciando xrequest(class_)
    
    # Finalizando iteracão
    except StopIteration:
        it.close()
        

if __name__ == '__main__':
    main()