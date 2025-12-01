
from dataclasses import dataclass


@dataclass
class Spedizione:
    id_hub_origine: int
    id_hub_destinazione: int
    guadagno: float
    conteggio: int

    def __eq__(self, other):
        return isinstance(other, Spedizione) and self.id == other.id

    def __str__(self):
        return f"{self.id_hub_origine} -> {self.id_hub_destinazione} : {self.guadagno}"

    def __repr__(self):
        return f"{self.id_hub_origine} -> {self.id_hub_destinazione} : {self.guadagno}"
