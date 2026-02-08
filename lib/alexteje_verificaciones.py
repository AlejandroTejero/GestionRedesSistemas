import os # Interactuar con el sistema
# Importo los mensajes de los errores
from alexteje_excepciones import PYTHONPATHError, ModuleMissingError

def verificar_pythonpath():
    # Explicacion funcion: Verificamos que PYTHONPATH incluye ~/lagrs/lib (bashrc), para poder ejecutar los modulos.

    # Obtenemos el valor que tiene guardado la variable PYTHONPATH
    pythonpath = os.environ.get("PYTHONPATH", "")
    # Construyo la ruta completa para poder usarse correctamnete
    lagrs_lib = os.path.expanduser("~/lagrs/lib")
    if lagrs_lib not in pythonpath.split(os.pathsep):
        # En caso de error lanzo mensaje
        raise PYTHONPATHError(f"El directorio {lagrs_lib} no está en PYTHONPATH.")

def verificar_modulos(login):
    # Explicacion funcion: Verifica que los módulos del usuario están en ~/lagrs/lib.
    
    # Construyo la ruta completa para poder usarse correctamnete
    lagrs_lib = os.path.expanduser("~/lagrs/lib")
    modulos_encontrados = False

    for archivo in os.listdir(lagrs_lib): # os.listdir; Obtengo una lista de los archivos que hay en lagrs_lib = direccion a lib
        if archivo.startswith(login) and archivo.endswith(".py"): # Compruebo que pertenecen al nombre y la extension correcta
            if not os.path.isfile(os.path.join(lagrs_lib, archivo)):
                # Si no es un archivo correcto (por ejemplo .txt)
                raise ModuleMissingError(f"El módulo {archivo} no es un archivo válido.")
            modulos_encontrados = True
            break  # Detenemos la búsqueda al encontrar un módulo válido

    # Si directamente no hay modulos
    if not modulos_encontrados:
        raise ModuleMissingError(f"No se encontraron módulos que comiencen con {login}.")

