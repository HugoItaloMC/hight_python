class Singleton(type):
    # Create type for instance control

    def __new__(meta, *args, **kwargs):
        # Behaviour to entailsen in childer object
        return type.__new__(meta, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        # Lonely instance
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance