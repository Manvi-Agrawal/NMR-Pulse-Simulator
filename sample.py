import numpy as np
from HamiltonianOperator import *

def O():
    a = (1j * np.pi/2 * Iy).expm()
    b = (1j * np.pi/2 * Ix).expm()
    c = (-1j * np.pi/2 * Iy).expm()
    d = (1j * np.pi/2 * Sy).expm()
    e = (1j * np.pi/2 * Sx).expm()
    f = (-1j * np.pi/2 * Sy).expm()
    g = (-1j * np.pi * IzSz).expm()
    return a*b*c*d*e*f*g
    #return g*f*e*d*c*b*a

print(O())