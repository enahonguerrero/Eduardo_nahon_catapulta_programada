"""Módulo con lógica simple de juego para lanzar proyectiles con la catapulta."""
from dataclasses import dataclass
import random
from .catapulta import Catapulta
from .simulacion import evaluar_catapulta


@dataclass
class ResultadoLanzamiento:
    distancia_m: float
    exito: bool


class Juego:
    def __init__(self, cat: Catapulta):
        self.cat = cat
        # Evaluación inicial
        self.estado = evaluar_catapulta(cat)

    def lanzar(self, tension: float, angulo_deg: float) -> ResultadoLanzamiento:
        """Simula un lanzamiento.

        tension: 0.0..1.0 (proporción de la fuerza máxima)
        angulo_deg: 0..90
        """
        fuerza = self.estado.fuerza / 10.0
        estabilidad = self.estado.estabilidad / 10.0

        # Factor aleatorio simula imprecisión
        imprec = random.uniform(0.85, 1.15) * (1.0 - 0.3 * (1.0 - estabilidad))

        # Física muy simplificada: alcance proporcional a fuerza * tension * sin(2*angulo)
        import math

        ang = math.radians(max(0, min(90, angulo_deg)))
        alcance = fuerza * tension * math.sin(2 * ang) * 10.0 * imprec

        # Scaling para acercarse a la estimación de la simulación
        alcance *= (self.estado.alcance_m / max(0.1, self.estado.alcance_m))

        distancia = round(max(0.0, alcance), 2)
        # Definir exito si distancia está dentro de una ventana objetivo (ej. 2..6 m)
        exito = 2.0 <= distancia <= 6.0
        return ResultadoLanzamiento(distancia_m=distancia, exito=exito)
