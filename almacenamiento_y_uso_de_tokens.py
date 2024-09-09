import re
from collections import Counter, defaultdict

# Definición de los patrones para los tipos de tokens
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
    posiciones_tokens = defaultdict(list)  # Almacenar posiciones de cada token
    contador_tokens = Counter()

    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Recorrer cada línea y encontrar los tokens
        for tipo, patron in patrones_tokens.items():
            for numero_linea, linea in enumerate(lineas, start=1):
                for match in re.finditer(patron, linea):
                    token = match.group()
                    posicion = f'línea {numero_linea}, posición {match.start() + 1}'
                    contador_tokens[(token, tipo)] += 1  # Contar ocurrencias del token por tipo
                    posiciones_tokens[(token, tipo)].append(posicion)  # Almacenar posiciones

        # Construir la tabla con TOKEN, TIPO, CANTIDAD y POSICIÓN
        resultado = "{:<15} {:<20} {:<10} {}\n".format("TOKEN", "TIPO", "CANTIDAD", "POSICIÓN")
        resultado += "-" * 70 + "\n"
        for (token, tipo), cantidad in contador_tokens.items():
            posiciones = ", ".join(posiciones_tokens[(token, tipo)])  # Combinar todas las posiciones
            resultado += "{:<15} {:<20} {:<10} {}\n".format(token, tipo, cantidad, posiciones)

    except FileNotFoundError:
        return "Archivo no encontrado."

    return resultado
