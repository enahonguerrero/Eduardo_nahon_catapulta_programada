# catapulta.py
"""Clase principal que contiene materiales y pasos de la catapulta."""
from typing import List, Optional
from material import Material
from paso import Paso

class Catapulta:
    def __init__(self, nombre: str = "Catapulta de cuchara") -> None:
        self.nombre: str = nombre
        self.materiales: List[Material] = []
        self.pasos: List[Paso] = []

    def agregar_material(self, material: Material) -> None:
        self.materiales.append(material)

    def agregar_paso(self, paso: Paso) -> None:
        self.pasos.append(paso)

    def listar_materiales(self) -> str:
        lines = [f"Materiales para '{self.nombre}':"]
        for m in self.materiales:
            lines.append(f"- {m}")
        return "\n".join(lines)

    def mostrar_pasos(self) -> str:
        header = f"Instrucciones paso a paso para '{self.nombre}':"
        pasos_txt = "\n".join(str(p) for p in self.pasos)
        return f"{header}\n\n{pasos_txt}"

    def marcar_paso(self, numero: int) -> bool:
        for p in self.pasos:
            if p.numero == numero:
                p.marcar_completado()
                return True
        return False

    def exportar_guia(self, ruta: str) -> str:
        contenido = f"{self.listar_materiales()}\n\n{self.mostrar_pasos()}"
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        return ruta

    def obtener_paso(self, numero: int) -> Optional[Paso]:
        for p in self.pasos:
            if p.numero == numero:
                return p
        return None
