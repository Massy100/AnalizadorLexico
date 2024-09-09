import re

caracteres_validos = [
    r'\b(entero|decimal|booleano|cadena|si|sino|mientras|hacer|verdadero|falso)\b',  # Palabras reservadas
    r'[\+\-\*\/\%]',  # Operadores
    r'[<>=]=?',  # Comparadores <, >, <=, >=, ==
    r'[\(\)\{\}\“\;]',  # Signos
    r'\b\d+\b',  # Números
    r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'  # Identificadores 
]

patron_valido = '|'.join(caracteres_validos)

patron_error = r'[^\w\s\+\-\*\/\%\=<>\"\(\)\{\};]'

def mostrar_errores(direccion_archivo):
    errores = []
    
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        for numero_linea, linea in enumerate(lineas, start=1):
            for match in re.finditer(patron_error, linea):
                errores.append(
                    f'Error: Caracter no permitido "{match.group()}" en la linea {numero_linea}, posicion {match.start() + 1}'
                )

        if not errores:
            return "No se detectaron errores."

    except FileNotFoundError:
        return "Archivo no encontrado."

    return "\n".join(errores)
