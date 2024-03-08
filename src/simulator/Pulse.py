from __future__ import annotations
from .Operator import Operator

class Pulse():
    def __init__(self, name, op, phase) -> None:
        self._name = name
        self._op = op
        self._phase = phase

    @property
    def name(self) -> str:
        return self._name

    def apply(self):
        return (-1j* self._phase * self._op).expm()
    
    def compile(self):
        return Operator(self.apply())