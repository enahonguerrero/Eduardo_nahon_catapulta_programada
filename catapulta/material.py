# material.py
"""Clase que representa un material necesario para la construcción."""
from dataclasses import dataclass

@dataclass
class Material:
    nombre: str
    cantidad: int = 1
    descripcion: str = ""

    def __str__(self) -> str:
        desc = f" ({self.descripcion})" if self.descripcion else ""
        return f"{self.cantidad} × {self.nombre}{desc}"
