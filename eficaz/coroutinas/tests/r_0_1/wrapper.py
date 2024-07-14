from weakref import WeakKeyDictionary

class Descritor:

    """
        Objeto controlador de chamadas de atributos 
      de instâncias utilizando protocolo descritor, 
      lembrando que este protocolo é utilizado para 
      atributos com regra  complexas,  para  regras 
      simples o decorator 'propety' pode  ser  uti-
      lizado tranquilamente.
    """

    def __init__(self):
        self._attr = WeakKeyDictionary()
    
    def __get__(self, instance, instance_type):
        if instance is None: return self.__set__(self)

        attr = self._attr.get(instance, 0)
        return self.__set__(attr)
    
    def __set__(self, instance, value):
        self._attr.get(instance, value)
    
    