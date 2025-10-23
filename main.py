# main.py
"""Programa principal: muestra materiales, pasos, permite marcar completados,
exportar y evaluar el estado de la catapulta según los materiales."""

from guia import crear_guia_catapulta_cuchara
from simulacion import evaluar_catapulta

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

    # 4️⃣ Bucle interactivo (opcional)
    while True:
        entrada = input(
            "\nIntroduce número de paso para marcar completado, 'e' para exportar, o 'q' para salir: "
        ).strip().lower()

        if entrada == "q":
            print("Saliendo. ¡Que te diviertas con la construcción segura!")
            break
        elif entrada == "e":
            ruta = catapulta.exportar_guia("guia_catapulta_cuchara.txt")
            print(f"Guía exportada a: {ruta}")
        else:
            try:
                num = int(entrada)
                if catapulta.marcar_paso(num):
                    print(f"Paso {num} marcado como completado.\n")
                    print(catapulta.mostrar_pasos())
                else:
                    print(f"No existe el paso {num}.")
            except ValueError:
                print("Entrada no válida. Introduce un número, 'e' o 'q'.")

if __name__ == "__main__":
    main()
