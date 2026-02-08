import os # Interactuar con el sistema
from optparse import OptionParser # Añadido para poder poner opciones al programa

# Añado modulos necesarios para el programa. El PYTONPATH esta en el bashrc
import alexteje_top as top
import alexteje_verificaciones as utils
from alexteje_excepciones import PYTHONPATHError, ModuleMissingError


def main():
    # El main simplemente se encarga de manejar las opciones

    parser = OptionParser(
        usage="usage: %prog [options]",
        description="Filtra y muestra información sobre procesos activos en el sistema."
    )
    # Opcion -u , --user
    parser.add_option("-u", "--user", dest="user", help="Filtrar procesos por usuario")
    # Opcion -t , --threshold
    parser.add_option(
        "-t", "--threshold", dest="threshold", type="float", default=0,
        help="Mostrar procesos con %CPU mayor al umbral especificado"
    )
    # Opcion -o , --output
    parser.add_option("-o", "--output", dest="output", help="Guardar la salida en un archivo")

    (options, args) = parser.parse_args()

    try:
        # Llamo a akexteje_verificaciones para filtar errores al principio
        utils.verificar_pythonpath()
        utils.verificar_modulos("alexteje")

        # Realizo el programa normal, descrito en alexteje_top
        salida_top = top.obtener_procesos()
        procesos = top.filtrar_procesos(
            salida_top, usuario=options.user, umbral_cpu=options.threshold
        )

        # Por si acaso no hay procesos con % > 0 de cpu, aunque siempre suelen existir
        if procesos:
            top.imprimir_procesos(procesos, archivo_salida=options.output)
        else:
            print("No se encontraron procesos que cumplan los criterios.")

    # Print de posibles excepciones que pueden salir
    except PYTHONPATHError as e:
        print(f"Error: {e}")
    except ModuleMissingError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == '__main__':
    main()

