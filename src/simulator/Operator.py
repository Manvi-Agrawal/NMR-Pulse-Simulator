from .DensityMatrix import DensityMatrix
import qutip as qt
import numpy as np

class Operator():
    def __init__(self) -> None:
        I = qt.identity(2)
        self._op = qt.tensor(I, I)
        self._rho_th = qt.Qobj(np.diag([1, 0.6, -0.6, -1]), dims=([[2, 2], [2, 2]]))

    def __init__(self, op: qt.Qobj) -> None:
        self._op = op
        self._rho_th = qt.Qobj(np.diag([1, 0.6, -0.6, -1]), dims=([[2, 2], [2, 2]]))


    def get_operator(self) -> qt.Qobj:
        return self._op

    def evolve_pho_th(self):
        return DensityMatrix(self._op * self._rho_th * self._op.dag())
    
    def evolve_pho(self, rho):
        return DensityMatrix(self._op * rho * self._op.dag())
