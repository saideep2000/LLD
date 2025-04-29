class RentalSystem():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalSystem, cls).__new__(cls)
            cls.__init__()
        return cls._instance
    def __init__(self):
        pass