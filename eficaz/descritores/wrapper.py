from weakref import WeakKeyDictionary

class Descritor:
    def __init__(self):
        self._attr = WeakKeyDictionary()
    
    def __get__(self, instance, instance_type):
        if instance is None: return self

        attr = self._attr.get(instance, 0)
        return self.__set__(attr)
    
    def __set__(self, instance, value):
        self._attr.get(instance, value)
    
    