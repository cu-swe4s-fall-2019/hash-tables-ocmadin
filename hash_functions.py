
def h_ascii(key, N):
    
    if key is None:
        raise TypeError('h_ascii: must supply a key')
    
    if not isinstance(key, str):
        raise TypeError('h_ascii: key must be a string')
    
    if N is None:
        raise TypeError('h_ascii: must supply a integer to N')
    
    if not isinstance(N, int):
        raise TypeError('h_ascii: N must be an integer')
        
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N


def h_rolling(key, N, p=53, m=2**64):
    
    if key is None:
        raise TypeError('h_ascii: must supply a key')
    
    if not isinstance(key, str):
        raise TypeError('h_ascii: key must be a string')
    
    if N is None:
        raise TypeError('h_ascii: must supply a integer to N')
    
    if not isinstance(N, int):
        raise TypeError('h_ascii: N must be an integer')   
    
    
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N 

