def analizar_sintaxis(direccion_archivo):
    
    errores_sintacticos = []
    
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas, start=1):
                if "function" in linea and "(" in linea:
                    parametros = linea.split('(')[1].split(')')[0].split(',')
                    if len(parametros) < 2:
                        errores_sintacticos.append(f"Error sintáctico en la línea {i}: Faltan parámetros en la función.")
    
    except FileNotFoundError:
        errores_sintacticos.append("Archivo no encontrado.")
    
    return errores_sintacticos
