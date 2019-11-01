import hash_functions
import sys
import random
import time

class LinearProbe:
    
    """
    LinearProbe hash table method
    
    ...
    
    Attributes
    ----------
    N : int
        Size of the hash table
    hash_function : function
        valid hash function to assign values to table locations
    T : list
        Hash table
    M : int
        Number of values in the table
    
    Methods
    -------
    add(key,value)
        Add a key-value pair to the hash table
    search(key)
        Find and retrieve a value for the provided key
    """
    def __init__(self, N, hash_function):
        if N is None:
            raise TypeError('LinearProbe: must supply a table size')
        if hash_function is None:
            raise TypeError('LinearProbe: must supply a hash function')

        if not isinstance(N, int):
            raise TypeError('LinearProbe: table size must be an integer')
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        pass


class ChainedHash:
    
    """
   ChainedHash hash table method
    
    ...
    
    Attributes
    ----------
    N : int
        Size of the hash table
    hash_function : function
        valid hash function to assign values to table locations
    T : list
        Hash table
    M : int
        Number of values in the table
    
    Methods
    -------
    add(key,value)
        Add a key-value pair to the hash table
    search(key)
        Find and retrieve a value for the provided key
    """
    
    
    def __init__(self, N, hash_function):

        if N is None:
            raise TypeError('ChainedHash: must supply a table size')
        if hash_function is None:
            raise TypeError('ChainedHash: must supply a hash function')

        if not isinstance(N, int):
            raise TypeError('ChainedHash: table size must be an integer')

        self.hash_function = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0


    def add(self, key, value):

        start_hash = self.hash_function(key, self.N)
        self.T[start_hash].append((key, value))
        self.M += 1
        return True
        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)

        for k, v in self.T[start_hash]:
            if key == k:
                return v
        return None

    def search_loc(self, key):
        start_hash = self.hash_function(key, self.N)

        for k, v in self.T[start_hash]:
            if key == k:
                return start_hash
        return None
        

def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val

'''
if __name__ == '__main__':

    N = int(sys.argv[1])
    hash_alg = sys.argv[2]
    collision_strategy = sys.argv[3]
    data_file_name= sys.argv[4]
    keys_to_add = int(sys.argv[5])

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_ascii)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_rolling)


    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('add', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break


    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)
        '''