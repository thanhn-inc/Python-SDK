from Crypto.Random import random

def rand_int64():
    return random.randint(0, 2**64 - 1)

def rand_interval(l, r):
    return random.randint(l, r)