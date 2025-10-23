# paso.py
"""Clase que representa un paso en la guía de montaje."""
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Paso:
    numero: int
    titulo: str
    descripcion: str
    duracion_aprox_min: Optional[int] = None
    completado: bool = field(default=False, init=False)

    def marcar_completado(self) -> None:
        """Marca el paso como completado."""
        self.completado = True

    def __str__(self) -> str:
        tiempo = f" (≈ {self.duracion_aprox_min} min)" if self.duracion_aprox_min else ""
        estado = "✅" if self.completado else "⬜"
        return f"{estado} Paso {self.numero}: {self.titulo}{tiempo}\n{self.descripcion}\n"
