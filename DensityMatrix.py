from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any

import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

def lorentian( w, w0,alpha, tau):
    #     n = 1 + 0.5*s + 4*(delta)*(delta)/(gamma*gamma)
        n = alpha*tau
        d = (1j)*(w-w0) + tau
        y = n/d
        return np.real(y)

class DensityMatrix():
    
    def __init__(self) -> None:
        self._rho = qt.tensor(I, I)
        (self._a,self._b,self._c,self._d) = np.diag(np.array(self._rho))


    def __init__(self, rho: qt.Qobj) -> None:
        self._rho = rho
        (self._a,self._b,self._c,self._d) = np.diag(np.array(rho))
      

    @property
    def rho(self):
        return self._rho
    
    def h_spectrum(self, wh=6.46, J=215.0):
        jh = J/62.37 # Divide by larmor freq of H to get ppm scale
        print("H spectrum")
        print(f"Peak1 at {np.around(wh-jh/2, 2)} ppm with integral={np.round(self._a-self._c, 2)}")
        print(f"Peak2 at {np.around(wh+jh/2, 2)} ppm with integral={np.round(self._b-self._d, 2)}")

    def h_pk1(self):
        return np.round(self._a-self._c, 2)

    def h_pk2(self):
        return np.round(self._b-self._d, 2)

        
    def plot_h_spectrum(self, ax, param_dict=None, wh=6.46, J=215.0, tau=0.016):
        jh = J/62.37 # Divide by larmor freq of H to get ppm scale
        

        w = np.linspace(0, 10, 1000)
        w0_pk1 = np.around(wh-jh/2, 2)
        alpha_pk1 = np.round(self._a-self._c, 2)
        y1= lorentian(w, w0_pk1, alpha_pk1, tau)

        w0_pk2 = np.around(wh+jh/2, 2)
        alpha_pk2 = np.round(self._b-self._d, 2)
        y2= lorentian(w, w0_pk2, alpha_pk2, tau)

        y = y1+y2

        plot = ax.plot(w, y, label=f"{w0_pk1} ppm={alpha_pk1} \n {w0_pk2} ppm={alpha_pk2}")
        ax.legend()
        return plot
        # plt.show()


    def c_spectrum(self, wc=73.331, J=215):
        jc = J/15.68 # Divide by larmor freq of C to get ppm scale
        print("C spectrum")
        print(f"Peak1 @ {np.around(wc-jc/2, 2)} ppm with integral={np.round(self._a-self._b, 2)}")
        print(f"Peak2 @ {np.around(wc+jc/2, 2)} ppm with integral={np.round(self._c-self._d, 2)}")

    def c_pk1(self):
        return np.round(self._a-self._b, 2)

    def c_pk2(self):
        return np.round(self._c-self._d, 2)

    def plot_c_spectrum(self, ax, param_dict=None, wc=73.331, J=215.0, tau=0.016):
        jc = J/15.68 # Divide by larmor freq of C to get ppm scale
        
        # print("C spectrum")

        w = np.linspace(60, 90, 1000)
        w0_pk1 = np.around(wc-jc/2, 2)
        alpha_pk1 = np.round(self._a-self._b, 2)
        y1= lorentian(w, w0_pk1, alpha_pk1, tau)

        w0_pk2 = np.around(wc+jc/2, 2)
        alpha_pk2 = np.round(self._c-self._d, 2)
        y2= lorentian(w, w0_pk2, alpha_pk2, tau)

        y = y1+y2
        plot = ax.plot(w, y, label=f"{w0_pk1} ppm={alpha_pk1} \n {w0_pk2} ppm={alpha_pk2}")

        # plot = ax.plot(w, y, label=f"a1={alpha_pk1}\n a2={alpha_pk2}")
        ax.legend()
        return plot
        # plt.show()

def main():
    rho = qt.Qobj(np.diag([1, 0.6, -1, -0.6]), dims=([[2, 2], [2, 2]]))
    d1 = DensityMatrix(rho)
    print("helo..")
    fig, ax = plt.subplots(1, 1)
    d1.plot_h_spectrum(ax, param_dict={})
    plt.show()
    # d1.h_spectrum()
    # d1.c_spectrum()

if __name__=="__main__": 
    main()