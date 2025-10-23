# guia.py
"""Función fábrica que crea la guía de la catapulta de cuchara (Opción A)."""
from .catapulta import Catapulta
from .material import Material
from .paso import Paso

def crear_guia_catapulta_cuchara() -> Catapulta:
    c = Catapulta()

    # Materiales (Opción A)
    c.agregar_material(Material("Cuchara de plástico o madera", 1, "cuchara de helado o cuchara de plástico"))
    c.agregar_material(Material("Banda(s) elástica(s)", 1, "puedes usar varias si son pequeñas"))
    c.agregar_material(Material("Pinza de la ropa (madera o plástico)", 1))
    c.agregar_material(Material("Base rígida pequeña", 1, "bloque de madera, tapa rígida o caja pequeña"))
    c.agregar_material(Material("Cinta adhesiva o pegamento fuerte", 1, "para fijar la pinza y la cuchara"))
    c.agregar_material(Material("Proyectiles blandos", 20, "algodón, pompones, o mini malvaviscos"))
    c.agregar_material(Material("Regla y cinta métrica", 1, "para medir distancias"))

    # Pasos
    c.agregar_paso(Paso(
        1,
        "Preparar la cuchara y la pinza",
        "Fija el mango de la cuchara a la parte móvil de la pinza de la ropa. Usa cinta o pegamento para que quede firme. "
        "Asegúrate de que la parte cóncava de la cuchara quede hacia fuera para sujetar el proyectil.",
        duracion_aprox_min=5
    ))
    c.agregar_paso(Paso(
        2,
        "Montar la pinza sobre la base",
        "Coloca la pinza con la cuchara montada sobre la base rígida. Pega o asegura la base de la pinza a la base para que actúe como bisagra. "
        "La pinza debe poder abrirse y cerrarse con cierta resistencia.",
        duracion_aprox_min=5
    ))
    c.agregar_paso(Paso(
        3,
        "Añadir la banda elástica",
        "Engancha una banda elástica desde el extremo de la cuchara hasta la base o enróllala en la parte superior de la pinza para proporcionar tensión. "
        "Ajusta según la fuerza deseada probando con proyectiles blandos.",
        duracion_aprox_min=5
    ))
    c.agregar_paso(Paso(
        4,
        "Pruebas iniciales y ajuste",
        "Haz pruebas desde distancias cortas (1–2 m). Ajusta la inclinación de la base y la tensión de la banda para cambiar la trayectoria. "
        "Si la banda es muy floja, la distancia será corta; si está muy tensa, reduce la tensión por seguridad.",
        duracion_aprox_min=10
    ))
    c.agregar_paso(Paso(
        5,
        "Seguridad y uso responsable",
        "No apuntes a personas ni animales. Usa sólo proyectiles blandos y mantén la catapulta alejada del rostro. Supervisa a menores si la usan.",
        duracion_aprox_min=2
    ))

    return c
