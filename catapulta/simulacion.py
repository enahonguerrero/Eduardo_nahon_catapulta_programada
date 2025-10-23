"""Módulo con heurísticas simples para evaluar la catapulta."""
from dataclasses import dataclass
from typing import Dict, List
from .catapulta import Catapulta


@dataclass
class EstadoCatapulta:
    fuerza: int
    estabilidad: int
    alcance_m: float
    resumen: Dict[str, str]
    recomendaciones: List[str]


def evaluar_catapulta(cat: Catapulta) -> EstadoCatapulta:
    """Evalúa de forma heurística la catapulta según materiales presentes.

    Basado en conteo y presencia de elementos, devuelve valores en 0..10.
    """
    fuerza = 0
    estabilidad = 0
    detalles: Dict[str, str] = {}

    names = [m.nombre.lower() for m in cat.materiales]

    # Fuerza: más bandas => más fuerza; cuchara presente da ventaja
    bandas = sum(m.cantidad for m in cat.materiales if "banda" in m.nombre.lower() or "elástica" in m.nombre.lower())
    if bandas >= 3:
        fuerza += 7
    elif bandas == 2:
        fuerza += 5
    elif bandas == 1:
        fuerza += 3

    if any("cuchara" in n for n in names):
        fuerza += 2
        detalles["cuchara"] = "Cuchara disponible: ayuda a sujetar proyectil"

    # Estabilidad: base rígida y pinza ayudan
    if any("base" in n for n in names) or any("bloque" in n for n in names):
        estabilidad += 4
    if any("pinza" in n for n in names):
        estabilidad += 3

    # Ajuste por cinta/pegamento
    if any("cinta" in n or "pegamento" in n for n in names):
        estabilidad += 2

    # Clamp values 0..10
    fuerza = max(0, min(10, fuerza))
    estabilidad = max(0, min(10, estabilidad))

    # Estimar alcance: heurística simple basada en fuerza y masa del proyectil
    masa_rel = 1.0
    if any("algodón" in n or "pompon" in n or "blandos" in n for n in names):
        masa_rel = 0.5
    alcance_m = round((fuerza * 0.8 + estabilidad * 0.2) * (1.0 / masa_rel) * 0.5, 2)

    resumen = {
        "bandas_elasticas": f"{bandas} banda(s)",
        "materiales_total": str(len(cat.materiales)),
        **detalles,
    }

    recomendaciones: List[str] = []
    if fuerza < 4:
        recomendaciones.append("Añade más bandas elásticas para aumentar la potencia.")
    if estabilidad < 5:
        recomendaciones.append("Fija mejor la pinza a una base sólida para mejorar la estabilidad.")
    recomendaciones.append("Realiza pruebas a corta distancia antes de aumentar la tensión.")

    return EstadoCatapulta(fuerza=fuerza, estabilidad=estabilidad, alcance_m=alcance_m, resumen=resumen, recomendaciones=recomendaciones)
