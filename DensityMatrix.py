from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any

import qutip as qt
import numpy as np

class DensityMatrix():
    
    def __init__(self) -> None:
        self._rho = qt.tensor(I, I)

    def __init__(self, rho: qt.Qobj) -> None:
        self._rho = rho
        (self._a,self._b,self._c,self._d) = np.diag(np.array(self._rho))
    
    @property
    def rho(self):
        return self._rho

    def h_spectrum(self, wh=6.46, J=215.0):
        jh = J/62.37 # Divide by larmor freq of H to get ppm scale
        print("H spectrum")
        print(f"Peak1 at {np.around(wh-jh/2,4)} ppm with integral={np.round(self._a-self._c, 4)}")
        print(f"Peak2 at {np.around(wh+jh/2,4)} ppm with integral={np.round(self._b-self._d, 4)}")

    def c_spectrum(self, wc=73.331, J=215):
        jc = J/15.68 # Divide by larmor freq of C to get ppm scale
        print("C spectrum")
        print(f"Peak1 @ {np.around(wc-jc/2,4)} ppm with integral={np.round(self._a-self._b)}")
        print(f"Peak2 @ {np.around(wc+jc/2,4)} ppm with integral={np.round(self._c-self._d)}")

def main():
    rho = qt.Qobj(np.diag([1, 0.6, -0.6, -1]), dims=([[2, 2], [2, 2]]))
    d1 = DensityMatrix(rho)
    print("helo..")
    d1.h_spectrum()
    d1.c_spectrum()

if __name__=="__main__": 
    main()