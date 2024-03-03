import qutip as qt

x = qt.sigmax()*0.5
y = qt.sigmay()*0.5
z = qt.sigmaz()*0.5
I = qt.qeye(2)

Ix = qt.tensor(x, I)
Iy = qt.tensor(y, I)
Iz = qt.tensor(z, I)

Sx = qt.tensor(I, x)
Sy = qt.tensor(I, y)
Sz = qt.tensor(I, z)

J = 215
tJ = 1/(2*J)
IzSz = qt.tensor(z, z)
