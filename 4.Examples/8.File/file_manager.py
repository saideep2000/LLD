class FileManager():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "initialised"):
            self.initialised = True
            