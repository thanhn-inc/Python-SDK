from Crypto.Random import random
import os

def rand_int64():
    return random.randint(0, 2**64 - 1)

def rand_interval(l, r):
    return random.randint(l, r)

def rand_bytes(length: int):
    """Returns a bytes object of the given input length.

    Args:
    
        length (int): Length of the required bytes object.
    """    
    return os.urandom(length)