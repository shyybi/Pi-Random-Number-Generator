from components.pi import *;
import random as rdm;

def prng():
    while True:
        prgn_generator = rdm.random();
        prng = f"{prgn_generator:.5f}".split('.')[1];
        if not prng.startswith('0'):
            break;
    return prng;
