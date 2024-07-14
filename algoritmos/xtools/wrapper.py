from typing import Generator


"""
  *** Busca Binária ***
  O algoritmo de busca binária tem como objetivo buscar um elemento
contido em um indice dentro de uma lista ordenada em ordem crescente,
este  algoritmo  executa as  tarefas  em logaritmo  O(log n) conforme 
aumenta suas operacões diminui o tempo de finalizacão. 
"""


class BinarySearch:

    def __init__(self, data: list, item):
        """
        - Essa funcão tem como objetivo
        buscar um valor e sua posicão de 
        indice em uma lista e  armazenar 
        o resultado em um dict  a  chave
        como posicão e valor o item bus-
        cado ficando assim, ex:
            -- {indice:item}
        params:
            data >> lista ordenada de forma linear
            item >> item para ser buscado dentro da lista 
        """
        self.data = data
        self.item = item


    def __iter__(self) -> Generator:
        
        low = 0
        high = len(self.data) - 1

        xdata = {}
        while low <= high:
            
            mind = int((high + low) / 2)

            find = self.data[mind]
            
            if find == self.item:
                xdata[mind] = find
                yield xdata
            
            if find > self.item:
                high = mind - 1
            else:
                low = mind + 1

        yield


"""
    ** Ordenacão por Selecão **
    - Algoritmo de ordenacão por selecão,
    tem como objetivo ordenar uma lista 
    com uma ordenacão linear de seus in-
    dices e respectivos valores
"""

class SortBySelection:

    def __init__(self, arr: list):
        self.arr: list = arr
    
    def __(self) -> Any:
        slarr = self.arr[0]
        smaller_idx = 0
        for line in range(1, len(self.arr)):
            if self.arr[line] < slarr:
                smaller_idx = line
        return smaller_idx    

if __name__ == '__main__':
    #data = [123213, 2323, 2233]
    #print(busca_binaria(data=data, item=2323))
    ...