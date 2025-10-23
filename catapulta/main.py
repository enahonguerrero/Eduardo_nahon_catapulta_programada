# main.py
"""Programa principal: muestra materiales, pasos, permite marcar completados y exportar."""
import argparse
from guia import crear_guia_catapulta_cuchara

def parse_args():
    parser = argparse.ArgumentParser(description="Guía interactiva: Catapulta de cuchara (Opción A)")
    parser.add_argument("--export", "-e", metavar="RUTA",
                        help="Exportar la guía a la ruta especificada (ej: guia.txt)")
    return parser.parse_args()

def main():
    args = parse_args()
    guia = crear_guia_catapulta_cuchara()

    print(guia.listar_materiales())
    print("\n" + "-"*60 + "\n")
    print(guia.mostrar_pasos())

    # Si se pide exportar por argumento, lo hacemos y salimos
    if args.export:
        ruta = guia.exportar_guia(args.export)
        print(f"\nGuía exportada a: {ruta}")
        return

    # Bucle interactivo por consola
    while True:
        entrada = input("\nIntroduce número de paso para marcar completado, 'e' para exportar la guía, 'r' para reiniciar marcas, o 'q' para salir: ").strip().lower()
        if entrada == 'q':
            print("Saliendo. ¡Que te diviertas con la construcción segura!")
            break
        elif entrada == 'e':
            ruta = guia.exportar_guia("guia_catapulta_cuchara.txt")
            print(f"Guía exportada a: {ruta}")
        elif entrada == 'r':
            # Reiniciar marcas
            for p in guia.pasos:
                p.completado = False
            print("Todas las marcas de pasos han sido reiniciadas.")
            print("\n" + guia.mostrar_pasos())
        else:
            try:
                num = int(entrada)
                if guia.marcar_paso(num):
                    print(f"Paso {num} marcado como completado.")
                    print("\n" + guia.mostrar_pasos())
                else:
                    print(f"No existe el paso {num}.")
            except ValueError:
                print("Entrada no válida. Introduce un número, 'e', 'r' o 'q'.")

if __name__ == "__main__":
    main()
