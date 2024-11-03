from src.factory.concret import Concret
__all__ = ['Factory', 'FactoryYY', 'FactoryNN']


# Factorys, herda de classes Concretas

class Factory(Concret): 
    flush: 'Handler' = ...  # Modifica atributos de saída e estado de toda instância
    def __init__(self, arg, *args, **kw):
        # `arg` dados enviados para serem trabalhados em Concret
        #       Qualquer alteracão em `arg` deve ser feita em objetos/funcões auxiliares em concret
        
        # `args` solicitacões de funcões/objetos auxiliares para `Concret`
        super().__init__(arg, *args)

        # `kw` atributos nível de Factory, 
        self.__kw = kw
    
    # Atributos dinâmicos
    def __getattr__(self, attr):
        valur = attr
        setattr(valur, self, attr)
        return valur



class FactoryXX(Factory):
    def __init__(self):
        super().__init__()



class FactoryYY(Factory):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    nn = ConcretN(set(range(1, 101)))
    nn.run()