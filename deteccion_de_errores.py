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
def mostrar_errores_sintacticos(direccion_archivo):
    errores_sintacticos = []
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
         
        for numero_linea, linea in enumerate(lineas, start=1):
            # Detección de errores sintácticos
            if linea.count(':') < linea.count('si'):
                errores_sintacticos.append(
                    f' Falta ":" en la línea {numero_linea}'
                )

        if not errores_sintacticos:
            return "No se detectaron errores."
        
    except FileNotFoundError:
        return "Archivo no encontrado."
    except Exception as e:  # Manejo de cualquier otra excepción
        return f"Se produjo un error: {str(e)}"

    return "\n".join(errores_sintacticos)
    
def mostrar_errores_semanticos(direccion_archivo):
    errores_semanticos = []
    funciones_declaradas = set()

    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        for numero_linea, linea in enumerate(lineas, start=1):
            # Detección de errores semánticos 
            # Comprobar declaración de variables
            if re.search(r'\b(entero|decimal|booleano|cadena)\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=', linea):  # Agregar paréntesis faltante
                var_declarada = re.findall(r'\b(entero|decimal|booleano|cadena)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=', linea)
                for tipo, nombre in var_declarada:
                    funciones_declaradas.add(nombre)  # Agregar a las funciones declaradas
            
            # Detección de división por cero
            if 'calcular_area' in linea and '0' in linea:
                errores_semanticos.append(
                    f'División por cero en la línea {numero_linea}'
                )
            
            # Validar uso de funciones
            for funcion in funciones_declaradas:
                if funcion not in linea:
                    errores_semanticos.append(
                        f'Función "{funcion}" no utilizada en la línea {numero_linea}'
                    )

        if not errores_semanticos:
            return "No se detectaron errores."

    except FileNotFoundError:
        return "Archivo no encontrado."
    except Exception as e:  # Manejo de cualquier otra excepción
        return f"Se produjo un error: {str(e)}"

    return "\n".join(errores_semanticos)



def mostrar_errores_lexicos(direccion_archivo):
    errores_lexicos = []
    
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        for numero_linea, linea in enumerate(lineas, start=1):
            # Detección de errores léxicos
            for match in re.finditer(patron_error, linea):
                errores_lexicos.append(
                    f'Caracter no permitido "{match.group()}" en la línea {numero_linea}, posición {match.start() + 1}'
                )
                

        if not errores_lexicos:
            return "No se detectaron errores."

    except FileNotFoundError:
        return "Archivo no encontrado."
    except Exception as e:  # Manejo de cualquier otra excepción
        return f"Se produjo un error: {str(e)}"

    return "\n".join(errores_lexicos)
