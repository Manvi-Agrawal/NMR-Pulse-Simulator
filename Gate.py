from Pulse import Pulse
import numpy as np
from PulseSequence import PulseSequence
from HamiltonianOperator import *

X_i = Pulse("Ix(pi)", Ix, np.pi)

X_s = Pulse("Sx(pi)", Sx, np.pi)

pH_i = Pulse("Iy(-pi/2)", Iy, -np.pi/2)

pH_i_dag = Pulse("Iy(+pi/2)", Iy, np.pi/2)

pH_s = Pulse("Sy(-pi/2)", Sy, -np.pi/2)

pH_s_dag = Pulse("Sy(+pi/2)", Sy, +np.pi/2)

aH_i = PulseSequence("Actual H_i")\
        .add(Pulse("Iy(+pi/2)", Iy, +np.pi/2))\
        .add(Pulse("Ix(+pi/2)", Ix, +np.pi/2))\
        .add(Pulse("Ix(+pi/2)", Ix, +np.pi/2))\

aH_s = PulseSequence("Actual H_s")\
        .add(Pulse("Sy(+pi/2)", Sy, +np.pi/2))\
        .add(Pulse("Sx(+pi/2)", Sx, +np.pi/2))\
        .add(Pulse("Sx(+pi/2)", Sx, +np.pi/2))\

def Iz_pulse(theta):
    return PulseSequence("Iz(theta)")\
        .add(Pulse("Ix(-pi/2)", Ix, -np.pi/2))\
        .add(Pulse(f"Iy({theta/np.pi}*pi)", Iy, theta))\
        .add(Pulse("Ix(pi/2)", Ix, np.pi/2))

def Sz_pulse(theta):
    return PulseSequence("Sz(theta)")\
        .add(Pulse("Sx(-pi/2)", Sx, -np.pi/2))\
        .add(Pulse(f"Sy({theta/np.pi}*pi)", Sy, theta))\
        .add(Pulse("Sx(pi/2)", Sx, np.pi/2))
   
cz_p = PulseSequence("CZ")\
    .add_seq(Iz_pulse(np.pi/2))\
    .add_seq(Sz_pulse(np.pi/2))\
    .add(Pulse("-2IzSz(aka delay(3/2J))", IzSz, 3*np.pi))

ncx = PulseSequence("Near CNOT")\
    .add(Pulse("Sx(pi/2)", Sx, np.pi/2))\
    .add(Pulse("2IzSz(aka delay(1/2J))", IzSz, np.pi))\
    .add(Pulse("Sy(-pi/2)", Sy, -np.pi/2))

cx =  PulseSequence("CNOT")\
    .add(pH_s)\
    .add_seq(cz_p)\
    .add(pH_s_dag)