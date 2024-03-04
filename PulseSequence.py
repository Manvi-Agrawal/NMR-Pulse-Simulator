from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any

import qutip as qt
import numpy as np
from Operator import Operator

class PulseSequence():
    def __init__(self, name) -> None:
        self.reset()
        self._name = name

    def reset(self) -> None:
        I = qt.identity(2)
        self._seq = []
        self._op = qt.tensor(I,I)

    @property
    def product(self) -> QObj:
        op = self._op
        self.reset()
        return op

    @property
    def name(self)-> str:
        return self._name

    def add(self, pulse: Pulse)->PulseSequence:
        self._seq.append(pulse.name)
        # print("Pulse op...")
        # print(pulse.apply())
        # print("self op...")
        # print(self._op)
        self._op = pulse.apply() * self._op
        return self
    
    def add_seq(self, seq1: PulseSequence)->PulseSequence:
        self._seq.extend(seq1._seq)
        # print("Pulse op...")
        # print(pulse.apply())
        # print("self op...")
        # print(self._op)
        self._op = seq1._op * self._op
        return self

    def print_sequence(self) -> None:
        print(f"{self._name} Pulse Sequence: {' -> '.join(self._seq)}", end="")
    
    def compile(self)-> Operator:
        return Operator(self._op)
