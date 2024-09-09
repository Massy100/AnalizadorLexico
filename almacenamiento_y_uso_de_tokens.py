import re
from collections import Counter

patrones_tokens = {
    'PALABRA RESERVADA': r'\b(entero|decimal|booleano|cadena|si|sino|mientras|hacer|verdadero|falso)\b',
    'OPERADOR': r'[\+\-\*\/\%\=<>]',
    'SIGNO': r'[\(\)\{\}\“\;]',
    'NUMERO': r'\b\d+\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
}

def clasificar_tokens(contenido):
    contador = Counter()

    for tipo, patron in patrones_tokens.items():
        for match in re.finditer(patron, contenido):
            contador[tipo] += 1

    return contador

def mostrar_tokens(direccion_archivo):
    tokens = []
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        contenido = ''.join(lineas)
        contador_tokens = clasificar_tokens(contenido)

        resultado = "Clasificacion y cantidad de tokens:\n"
        for tipo, cantidad in contador_tokens.items():
            resultado += f'{tipo}: {cantidad}\n'

        resultado += "\nTokens encontrados:\n"

        for tipo, patron in patrones_tokens.items():
            for numero_linea, linea in enumerate(lineas, start=1):
                for match in re.finditer(patron, linea):
                    tokens.append(f'{tipo} "{match.group()}" en la linea {numero_linea}, posicion {match.start() + 1}')

        resultado += "\n".join(tokens)

    except FileNotFoundError:
        return "Archivo no encontrado."

    return resultado

