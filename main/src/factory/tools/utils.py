class Utils:

    def __init__(self, *args: tuple):
        super().__init__()
        self.__args = args
    
    def __call__(self):
        for line in self.__args:
            print(line)