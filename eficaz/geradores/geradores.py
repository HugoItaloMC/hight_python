"""
  - Um gerador não são, de verdade, executados.
  Em vez disso retornam um itarador, em cada 
  chamada à funcão nativa next() ou send(), lem-
  brando que para iniciar o gerador devemos uti-
  lizar o next(), o próximo yield e chamado
"""
from typing import Generator, Tuple
from collections import namedtuple
from itertools import islice

Data = namedtuple('Data', ('name', 'passwd', 'email'))
Request = namedtuple('Request', ('method', 'data'))


def xrequest(args: Tuple[Generator]):
    """
     - Recebe um generator expression
     itera sobre ele e verifica condi-
     cionais externas contratadas.
    
    return:
        yield 
     
    
    params:
        args: namedtuple(colletions)
          args[0]: method
          args[1]: data: tuple

    """

    arg = next(args)  # recolhendo primeiro argumento 'method HTTP'
    print(arg)
    if any(arg) and 'POST' in arg:
        print(args.send(True).name)  # recolhendo o segundo argumento data=tuple
    
    #for arg in args:  # Aqui descartamos o primeiro argumento do generator
        #if any(arg) and 'POST' in arg:
            #for data in args:
            #    print(data)
            #if not arg:
                #yield count

if __name__ == '__main__':

    # ESTRUTURA DE DADOS
    data = Data(name='nameHugo', passwd='passwdHugo', email='hugoEmail')   

    get = (get for get in Request(method='GET', data=data))
    post = (post for post in Request(method='POST', data=data))
    ########

    # ENVIANDO REQUISICÃO
    #result = islice(xrequest(args=post), None)
    #print(''.join(map(str, result)))
    #######

    xrequest(args=post)