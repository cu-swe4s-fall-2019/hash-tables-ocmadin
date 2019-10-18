# Hash tables


## Contents

`hash_functions.py` contains the `h_ascii` and `h_rolling` hash functions.

These functions are implementations of two different hashing strategies.

`hash_tables.py` contains the `LinearProbe` and `ChainedHash` classes.
These classes initialize a hash table with a given size and hash function, and allows users to insert new values with `add`, and search values based on a key with `search`

`benchmark.sh` contains routines to run benchmarks hash function randomness, as well as the load factors and search times for the LinearProbe method.

`rand_works.txt` and `non_rand_works.txt` are used in these tests.
