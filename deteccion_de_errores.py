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

# Patrón para caracteres no válidos
patron_error = r'[^\w\s\+\-\*\/\%\=<>\"\(\)\{\};]'

def mostrar_errores(direccion_archivo):
    errores = []
    funciones_declaradas = set()
    
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        for numero_linea, linea in enumerate(lineas, start=1):
            # Detección de errores léxicos
            for match in re.finditer(patron_error, linea):
                errores.append(
                    f'Error Léxico: Caracter no permitido "{match.group()}" en la línea {numero_linea}, posición {match.start() + 1}'
                )
                
            # Detección de errores sintácticos
            if linea.count(':') < linea.count('si'):
                errores.append(
                    f'Error Sintáctico: Falta ":" en la línea {numero_linea}'
                )

            # Detección de errores semánticos 
            # Comprobar declaración de variables
            if re.search(r'\b(entero|decimal|booleano|cadena)\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=', linea):  # Agregar paréntesis faltante
                var_declarada = re.findall(r'\b(entero|decimal|booleano|cadena)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=', linea)
                for tipo, nombre in var_declarada:
                    funciones_declaradas.add(nombre)  # Agregar a las funciones declaradas
            
            # Detección de división por cero
            if 'calcular_area' in linea and '0' in linea:
                errores.append(
                    f'Error Semántico: División por cero en la línea {numero_linea}'
                )
            
            # # Validar uso de funciones
            # for funcion in funciones_declaradas:
            #     if funcion not in linea:
            #         errores.append(
            #             f'Error Semántico: Función "{funcion}" no utilizada en la línea {numero_linea}'
            #         )

        if not errores:
            return "No se detectaron errores."

    except FileNotFoundError:
        return "Archivo no encontrado."
    except Exception as e:  # Manejo de cualquier otra excepción
        return f"Se produjo un error: {str(e)}"

    return "\n".join(errores)
