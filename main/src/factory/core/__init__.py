# Pythoon defaults imports
from abc import abstractmethod

__all__ = ['SuperClass']  # CONTROLANDO IMPORTACÃO DO MÓDULO

class Descriptor:
    # Descriptor object from `SuperClass`

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance):
        raise AttributeError("%s Attr just read" % self.name)
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return lambda: next(instance())


class Meta(type):
    # Metaclasse, controlando atributos
    def __new__(meta, name, bases, attrs):
        if 'run' in attrs and attrs['run'] is ...:
            attrs['run'] = Descriptor()  # Fazendo refrência através do protocolo descritor
        return type.__new__(meta, name, bases, attrs)
    
    def __call__(cls, *arg, **kw):
        # singleton, isolando instâncias
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Meta, cls).__call__(*arg, **kw)
        return cls.__instance


class AbstractPro(metaclass=Meta):
    # Superclasse contento atributos e métodos em comun entre as subclasses

    def __init__(self):
        self._exit  = 0  # Controlador de saída
        self._state = False  # Controlador de estado

    # //// GERENCIANDO SAÍDAS E ESTADO ATRAVÉS DE OPERADORES UNÁRIOS /////
    def __pos__(self):                #      OPERADOR POSITIVO :         #
        if not self._exit:            #       exemplo: obj = Class(25)   #
            self._exit += 1           #            print(+obj) ; 25      #
        return self._exit             #                                  #
                                      ####################################      
    def __neg__(self):                #      OPERADOR NEGATIVO:          #  
        self._exit -= 1               #      exemplo: obj = Class(25)    #
        return self._exit             #          print(~obj) ; -25       #
                                      #                                  #
                                      ####################################
    def __invert__(self):             #   MUDANCA DE ESTADO BIT A BIT    #
        self._state = not self._state #      exemplo: obj = Class()      #
        return self._state            #      print(~obj) ; True          #
                                      #      print(~obj) ; False         #
    ######################################################################

    def __call__(self):
        while True:
            try:
                next(self)
            except StopIteration:
                +self  # SAÍDA 1  para conclusão bem sucedida
                ~self  # MUDANDO O ESTADO DO OBJETO BIT A BIT, ESSA MUDANCA TB PODE OCORRER EM CONTRATOS EXTERNOS
                yield (self._exit, self._state,)
    @abstractmethod             
    def __next__(self):
        raise NotImplementedError("MÉTODO NÃO IMPLEMENTADO")

