import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        return archivo
    

def mostrar_archivo():
    return abrir_archivo()


