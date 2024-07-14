import os  # Uso para caso genérico de dados
import json
from random import choice  # Uso para caso genérico de dados
from typing import SupportsInt, Iterable, Generator, Dict

from wrapper import BinarySearch  # algoritmos de estudo


class PullJson:

    """
     - Recebe  os  dados do tipo dict
     o formata  para  estrutura  json
     e armazena em um arquivo externo
     no formato json
    """
    
    def __init__(self, path, data: dict):
        """
            path: Caminho do arquivo para armazenar os dados
            data: Type(dict)  dados  recebidos  externamente
        """
        self.path = path
        self.data = data
        
        #self.FILES_ALLOWEDS = re.finditer(pattern=r"*.\.(xlsx|json|csv)", flags=re.NOFLAG, string=self.path.name)

    def __call__(self) -> Dict:
        with open(self.path, "a+") as filerr:
            self.__next__(filerr.write('\n%s' % self.__iter__()))
            
    
    def __iter__(self):
        if self.data:
            return json.dumps(self.data, ensure_ascii=False)
        else:
            return json.dumps({'non-valur': 'Valor ñ encontrado'}, ensure_ascii=False)
    
    def __coroutine(self):
        while True:
            yield
    
    def __next__(self, *args):
        coroutine = self.__coroutine()
        next(coroutine)
        for line in args:
            coroutine.send(line)
        coroutine.close()

class WrapperUtils:
    """
      - Recebe  dados, armazena  em uma lista
      para  c aso  genérico no  construtor os
      dados  estão sendo  gerados, mas  em um
      caso  real os  dados  partiriam  de uma
      fonte  externa uma API ou  um  banco de 
      dados. 
    """

    def __init__(self):
        #  - Gerando Dados aleatórios na construcão do objeto

        self.__bdata: SupportsInt = os.urandom(2)  # Gerando números aleatórios, como binários
        self.__sdata: str = ''.join(map(str, self.__bdata)) # Modificando valores binários para string
        self.__data: Iterable = range(1, int(self.__sdata), 1)  # Gerando um range de até o valor randomico gerado
        self.item: Iterable = choice(list(self.__data) * int(len([self.__data]))) # Escolhendo um valor para buscar na estrutura de dados      

    def __iter__(self) -> Generator:
        while True:
            yield


    def __next__(self, *arg) -> None:
        coroutine = self.__iter__()   # Iniciando coroutina
        next(coroutine)
        for line in arg:
            coroutine.send(line)  # Respondendo a sinais externos
        coroutine.close()        

    def __call__(self):
        xdata = []  # Para armazenar os dados de forma desordenada
        ldata = list(self.__data)
        # Desordenando os valores dos indices para caso de estudo
        for _ in range(1, len(ldata), 1):
            while len(xdata) < len(ldata):
                self.__next__(xdata.append(choice(ldata)))
        
        xdata.sort() # Ordenando valores de forma linear
        
        """
            - Lembrando que o algoritmo de busca binária
            busca valores  armazenados de  forma  linear 
            crescente, ex:
                -- Ana, Bruno, Carlos (alfabética)
                -- 10, 11, 12, 25, 44 (numérica)
        """
        # Utilizando ** Busca Binária **
        for line in BinarySearch(data=xdata, item=self.item):
            return line
        
            
        # Busca utilizando o método index() do tipo lista
        #return {xdata.index(self.item, 0): self.item}
        
    
    
    #def __str__(self):
    #    self.dtdata

if __name__ == '__main__':
    while True:
       PullJson('xtools/db/data.json', WrapperUtils()())()
