
from PulseSequence import PulseSequence

from Gate import *
import matplotlib.pyplot as plt

class Algorithm():
    def __init__(self, name):
        self._name = name

        self._p0 = PulseSequence("P0")

        self._p1 = PulseSequence("P1")\
        .add(Pulse("Sx(+pi/2)", Sx, +np.pi/2))\
        .add(Pulse("2IzSz(aka delay(1/2J))", IzSz, +np.pi))\
        .add(Pulse("Sy(+pi/2)", Sy, +np.pi/2))\
        .add(Pulse("Ix(+pi/2)", Ix, +np.pi/2))\
        .add(Pulse("2IzSz(aka delay(1/2J))", IzSz, +np.pi))\
        .add(Pulse("Iy(+pi/2)", Iy, +np.pi/2))\
        
        self._p2 = PulseSequence("P2")\
        .add(Pulse("Ix(+pi/2)", Ix, +np.pi/2))\
        .add(Pulse("2IzSz(aka delay(1/2J))", IzSz, +np.pi))\
        .add(Pulse("Sx(+pi/2)", Sx, +np.pi/2))\
        .add(Pulse("Iy(+pi/2)", Iy, +np.pi/2))\
        .add(Pulse("2IzSz(aka delay(1/2J))", IzSz, +np.pi))\
        .add(Pulse("Sy(+pi/2)", Sy, +np.pi/2))\
        
        self._seq = PulseSequence(self._name)

    def state_prep(self, state):
        if state=="00":
            self._p0.add(X_i).add(X_s)
            self._p1.add(X_i).add(X_s)
            self._p2.add(X_i).add(X_s)
            return self

        elif state=="01":
            self._p0.add(X_i)
            self._p1.add(X_i)
            self._p2.add(X_i)
            return self

        elif state=="10":
            self._p0.add(X_s)
            self._p1.add(X_s)
            self._p2.add(X_s)
            return self


        elif state=="11":
            self._p0 = self._p0
            self._p1 = self._p0
            self._p2 = self._p0
            return self

        else:
            raise ValueError(f"Incorrect state : {state}")
        
    def add_sequence(self, algo_seq):
        self._p0.add_seq(algo_seq)
        self._p1.add_seq(algo_seq)
        self._p2.add_seq(algo_seq)
        return self

    def add_pulse(self, algo_pulse):
        self._p0.add(algo_pulse)
        self._p1.add(algo_pulse)
        self._p2.add(algo_pulse)
        return self

    
    def execute_algorithm(self):
        self._p0.print_sequence()
        print("\n")
        self._p1.print_sequence()
        print("\n")
        self._p2.print_sequence()


        fig, axs = plt.subplots(2, 3, sharey="row", figsize=(10,8))
        # fig = plt.figure(figsize=(8, 6))

        p0_sim = self._p0.compile().evolve_pho_th()


        p0_sim.plot_h_spectrum(axs[0,0], param_dict={})
        p0_sim.plot_c_spectrum(axs[1,0], param_dict={})
        axs[0,0].set_title("P0-1H")
        axs[1,0].set_title("P0-13C")


        p1_sim = self._p1.compile().evolve_pho_th()
        p1_sim.plot_h_spectrum(axs[0,1], param_dict={"label":"hi"})
        p1_sim.plot_c_spectrum(axs[1,1], param_dict={})
        axs[0,1].set_title("P1-1H")
        axs[1,1].set_title("P1-13C")


        p2_sim = self._p2.compile().evolve_pho_th()
        p2_sim.plot_h_spectrum(axs[0,2], param_dict={})
        p2_sim.plot_c_spectrum(axs[1,2], param_dict={})
        axs[0,2].set_title("P2-1H")
        axs[1,2].set_title("P2-13C")

        pho_net = (p0_sim.rho+p1_sim.rho+p2_sim.rho)/3

        p0_h_pk1 = p0_sim.h_pk1()
        p1_h_pk1 = p1_sim.h_pk1()
        p2_h_pk1 = p2_sim.h_pk1()
        h_pk1 = (p0_h_pk1 + p1_h_pk1 + p2_h_pk1)/3
        h_pk1 = np.round(h_pk1, 3)

        p0_h_pk2 = p0_sim.h_pk2()
        p1_h_pk2 = p1_sim.h_pk2()
        p2_h_pk2 = p2_sim.h_pk2()
        h_pk2 = (p0_h_pk2 + p1_h_pk2 + p2_h_pk2)/3
        h_pk2 = np.round(h_pk2, 3)


        p0_c_pk1 = p0_sim.c_pk1()
        p1_c_pk1 = p1_sim.c_pk1()
        p2_c_pk1 = p2_sim.c_pk1()
        c_pk1 = (p0_c_pk1 + p1_c_pk1 + p2_c_pk1)/3
        c_pk1 = np.round(c_pk1, 3)


        p0_c_pk2 = p0_sim.c_pk2()
        p1_c_pk2 = p1_sim.c_pk2()
        p2_c_pk2 = p2_sim.c_pk2()
        c_pk2 = (p0_c_pk2 + p1_c_pk2 + p2_c_pk2)/3
        c_pk2 = np.round(c_pk2, 3)


        print("Resultant Matrix::")
        print(pho_net)

        h_spectrum = f"H net spectrum: {h_pk1}, {h_pk2}"
        c_spectrum = f"C net spectrum: {c_pk1}, {c_pk2}"

        print(h_spectrum)
        print(c_spectrum)



        fig.suptitle(f"{self._name} \n {h_spectrum} \n {c_spectrum}")
        # axs[0]
        plt.legend()
        plt.show()

        
    

def main():
    print("start")
    ta = Algorithm("Tempoaral Averaging -- |00>")
    ta.state_prep("00")
   

    ta.execute_algorithm()
    print("\nend")



if __name__=="__main__":
    main()

