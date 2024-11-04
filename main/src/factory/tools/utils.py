class PairNumber:

    def __init__(self, arg: set):
        super().__init__()
        self.__arg = arg
    
    def __call__(self):
        self.__arg = {x for x in self.__arg if x % 2 == 0}
        return self.__arg