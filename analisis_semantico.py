def analizar_semantica(direccion_archivo):
    errores_semanticos = []
    
    try:
        with open(direccion_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas, start=1):
                if "int" in linea and "=" in linea:
                    variable = linea.split()[1]
                    if any(palabra for palabra in lineas if variable in palabra and "string" in palabra):
                        errores_semanticos.append(f"Error semántico en la línea {i}: Variable {variable} declarada como int pero usada como string.")
    
    except FileNotFoundError:
        errores_semanticos.append("Archivo no encontrado.")
    
    return errores_semanticos
