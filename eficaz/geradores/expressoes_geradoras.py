"""
  - Expressões geradoras abrangentes utilizam 
  um  elemento  de  iteracão que  captura  um 
  item por vez, diferente de uma lista abran-
  gente que captura todos  elementos e  assim 
  consumindo mais recursos computacionais.
"""
from collections import namedtuple

Data = namedtuple('Data', ('name', 'passwd', 'email'))
Request = namedtuple('Request', ('method', 'data'))


if __name__ == '__main__':

    data = Data(name='nameHugo', passwd='passwdHugo', email='hugoEmail')
    
    post = Request(method='POST', data=data)
    get = Request(method='GET', data=data)
    
    it = (x for x in [post, get])  # Expressão geradora
    
    while True:
        try:

            # Após iniciarmos o generator com método next() utilizamos o send() para buscar o próximo elemento
            post = next(it)
            get = it.send(True)
            print(post, get)
        except StopIteration:
            it.close()
            break