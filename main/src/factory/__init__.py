from src.factory.abs import Abstract
__all__ = ['Factory']


class Concret(Abstract):
    # Classe AbstractFactory, aqui controlamos atributos de baixo nível
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


# Factory, herda de classes Concretas
class Factory(Concret):
    # Concret Factory
    # Aqui podemos controla atributos ou métodos de alto nível

    def __init__(self, arg, *args, **kw):
        super().__init__(arg, *args, **kw)
    
    def __getattr__(self, attr):
        return super().__getattr__(attr)


if __name__ == '__main__':
    nn = ConcretN(set(range(1, 101)))
    nn.run()