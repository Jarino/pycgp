class Counter:
    instance = None

    def __init__(self):
        self.same_as_original = 0
        self.dict = {}
    
    @staticmethod
    def get():
        if Counter.instance is None:
            Counter.instance = Counter()
        
        return Counter.instance
            

