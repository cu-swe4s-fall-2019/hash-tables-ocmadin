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

        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

        
        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        pass

class ChainedHash:
    def __init__(self, N, hash_function):
        
        if N is None:
            raise TypeError('ChainedHash: must supply a table size')
        if hash_function is None:
            raise TypeError('ChainedHash: must supply a hash function')
            
        if not isinstance(N, int):
            raise TypeError('ChainedHash: table size must be an integer')
        self.hash_function = hash_function
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        pass


