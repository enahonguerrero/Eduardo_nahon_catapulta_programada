# main.py
"""Programa principal: muestra materiales, pasos, permite marcar completados,
exportar y evaluar el estado de la catapulta según los materiales."""

from catapulta import crear_guia_catapulta_cuchara
from catapulta.simulacion import evaluar_catapulta
from catapulta.juego import Juego

def main():
    # 1️⃣ Crear la catapulta (instanciando la guía completa)
    catapulta = crear_guia_catapulta_cuchara()

    # 2️⃣ Mostrar materiales y pasos
    print(catapulta.listar_materiales())
    print("\n" + "-" * 60 + "\n")
    print(catapulta.mostrar_pasos())

    # 3️⃣ Evaluar comportamiento según materiales
    estado = evaluar_catapulta(catapulta)

    print("\n" + "=" * 40)
    print("EVALUACIÓN DE LA CATAPULTA (heurística):")
    print(f"Fuerza (0..10): {estado.fuerza}")
    print(f"Estabilidad (0..10): {estado.estabilidad}")
    print(f"Alcance estimado (m) para proyectiles blandos: {estado.alcance_m}")
    print("\nDetalles:")
    for k, v in estado.resumen.items():
        print(f" - {k}: {v}")
    print("\nRecomendaciones:")
    for r in estado.recomendaciones:
        print(f" * {r}")
    print("=" * 40)

    juego = Juego(catapulta)

    # 4️⃣ Bucle interactivo
    while True:
        print("\n" + "=" * 40)
        print("Menú - Catapulta de cuchara")
        print("1. Ver materiales y pasos")
        print("2. Marcar paso como completado")
        print("3. Exportar guía a fichero")
        print("4. Evaluar catapulta (heurística)")
        print("5. Jugar: lanzar proyectil")
        print("q. Salir")
        choice = input("Selecciona una opción: ").strip().lower()

        if choice == "q":
            print("Saliendo. ¡Que te diviertas con la construcción segura!")
            break
        if choice == "1":
            print(catapulta.listar_materiales())
            print("\n" + "-" * 60 + "\n")
            print(catapulta.mostrar_pasos())
        elif choice == "2":
            try:
                num = int(input("Número de paso a marcar: "))
                if catapulta.marcar_paso(num):
                    print(f"Paso {num} marcado como completado.")
                else:
                    print("Paso no encontrado.")
            except ValueError:
                print("Entrada no válida.")
        elif choice == "3":
            ruta = catapulta.exportar_guia("guia_catapulta_cuchara.txt")
            print(f"Guía exportada a: {ruta}")
        elif choice == "4":
            estado = evaluar_catapulta(catapulta)
            print("\n" + "=" * 40)
            print("EVALUACIÓN DE LA CATAPULTA (heurística):")
            print(f"Fuerza (0..10): {estado.fuerza}")
            print(f"Estabilidad (0..10): {estado.estabilidad}")
            print(f"Alcance estimado (m): {estado.alcance_m}")
            print("\nDetalles:")
            for k, v in estado.resumen.items():
                print(f" - {k}: {v}")
            print("\nRecomendaciones:")
            for r in estado.recomendaciones:
                print(f" * {r}")
            print("=" * 40)
        elif choice == "5":
            try:
                tension = float(input("Tensión (0.0 - 1.0): "))
                ang = float(input("Ángulo (grados 0-90): "))
                res = juego.lanzar(tension, ang)
                print(f"Distancia obtenida: {res.distancia_m} m")
                print("¡Éxito!" if res.exito else "No alcanzó la zona objetivo.")
            except ValueError:
                print("Entradas no válidas para tensión o ángulo.")
        else:
            print("Opción no reconocida.")

if __name__ == "__main__":
    main()
