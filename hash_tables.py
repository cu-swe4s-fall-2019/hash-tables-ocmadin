import hash_functions

class LinearProbe:
    def __init__(self, N, hash_function):
        if N is None:
            raise TypeError('LinearProbe: must supply a table size')
        if hash_function is None:
            raise TypeError('LinearProbe: must supply a hash function')
            
        if not isinstance(N, int):
            raise TypeError('LinearProbe: table size must be an integer')
        self.hash_function = hash_function
        self.N = N
        self.T = [ None for i in range(N) ]
        self.M = 0


    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        
        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        pass

class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        pass


