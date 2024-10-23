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
                    f'Falta ":" en la línea {numero_linea}'
                )
        
            # Detección de división por cero
            if 'calcular_division' in linea and ', 0' in linea:
                errores_sintacticos.append(
                    f'División por cero en la línea {numero_linea}'
                )

            if 'decimal' in linea and '(' in linea:
                for  numero_linea2, linea2 in enumerate(lineas[numero_linea:], start=numero_linea):
                    if '}' in linea2:
                        break
                    if 'return' in linea2 and '"' in linea2:
                        errores_sintacticos.append(
                        f'Retorno de variable str en decimal en la línea {numero_linea2}'
                        )
                        break
            
            if 'decimal' in linea and '=' in linea and '"' in linea:
                errores_sintacticos.append(
                        f'Ingreso de str en un decimal en la línea {numero_linea2}'
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
            max_linea = len(lineas)

        for numero_linea, linea in enumerate(lineas, start=1):
            # Detección de errores semánticos 
            # Comprobar declaración de variables
            if re.search(r'\b(entero|decimal|booleano|cadena)\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=', linea):  # Agregar paréntesis faltante
                var_declarada = re.findall(r'\b(entero|decimal|booleano|cadena)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=', linea)
                for tipo, nombre in var_declarada:
                    funciones_declaradas.add(nombre)  # Agregar a las funciones declaradas
            
            if '(' in linea and ')' not in linea:
                    errores_semanticos.append(
                    f'Parentesis no cerrado en linea {numero_linea}'
                    )
            if '[' in linea and ']' not in linea:
                    errores_semanticos.append(
                    f'Corchetes no cerrado en linea {numero_linea}'
                    )

            if '{' in linea and '}' in linea:
                errores_semanticos.append(
                        f'Llaves cerrando en la misma linea {numero_linea}'
                        )

            if '{' in linea:
                for  numero_linea2, linea2 in enumerate(lineas[numero_linea:], start=numero_linea):
                    if '}' in linea2:
                        break
                    if '{' in linea2: #ESTO ESGA MAL PARA EL FUTURO !!! ALERTA PIDELE A MASSY QUE O RESUELVA ELLA SI HIZO EL EXAMEN FINAL DE LAB
                        errores_semanticos.append(
                        f'Llaves no cerradas {numero_linea2}'
                        )
                    if numero_linea2 == max_linea and '}' not in linea2:
                        errores_semanticos.append(
                        f'Llaves nunca cerradas {numero_linea2}'
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
