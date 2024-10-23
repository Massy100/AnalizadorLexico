import tkinter as tk
from tkinter import ttk
import busqueda_del_archivo
import deteccion_de_errores
import almacenamiento_y_uso_de_tokens
import analisis_sintactico
import analisis_semantico

def main():
    class ListboxFrame(ttk.Frame):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
            self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
            self.listbox = tk.Listbox(
                self,
                height=10,
                width=100,
                xscrollcommand=self.hscrollbar.set,
                yscrollcommand=self.vscrollbar.set
            )
            self.hscrollbar.config(command=self.listbox.xview)
            self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            self.vscrollbar.config(command=self.listbox.yview)
            self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.listbox.pack()

    def efectos_al_mostrar_archivo():
        direccion = busqueda_del_archivo.mostrar_archivo()
        mostrar_archivo(direccion)
        mostrar_deteccion_de_error(direccion)  # Errores léxicos
        # mostrar_errores_sintacticos(direccion)  # Errores sintácticos
        # mostrar_errores_semanticos(direccion)  # Errores semánticos
        mostrar_tokens(direccion)  # Tokens

    def mostrar_archivo(direccion):
        linea = ""
        listbox_frame.listbox.delete(0, tk.END)
        try:
            with open(direccion, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                for i in contenido:
                    if i == "\n":
                        listbox_frame.listbox.insert(tk.END, (linea))
                        linea = ""
                    linea += i
                listbox_frame.listbox.insert(tk.END, (linea))
        except FileNotFoundError:
            listbox_frame.listbox.insert(tk.END, "Archivo no encontrado.")

    def mostrar_deteccion_de_error(direccion):
        linea = ""
        texto_le = deteccion_de_errores.mostrar_errores_lexicos(direccion)
        texto_se = deteccion_de_errores.mostrar_errores_semanticos(direccion)
        texto_si = deteccion_de_errores.mostrar_errores_sintacticos(direccion)
        listbox_frame2.listbox.delete(0, tk.END)
        listbox_frame4.listbox.delete(0, tk.END)
        listbox_frame5.listbox.delete(0, tk.END)
        for i in texto_le:
            if i == "\n":
                listbox_frame2.listbox.insert(tk.END, (linea))
                linea = ""
            linea += i
        listbox_frame2.listbox.insert(tk.END, (linea))

        linea = ""
        for i in texto_si:
            if i == "\n":
                listbox_frame4.listbox.insert(tk.END, (linea))
                linea = ""
            linea += i
        listbox_frame4.listbox.insert(tk.END, (linea))

        linea = ""
        for i in texto_se:
            if i == "\n":
                listbox_frame5.listbox.insert(tk.END, (linea))
                linea = ""
            linea += i
        listbox_frame5.listbox.insert(tk.END, (linea))

    def mostrar_tokens(direccion):
        linea = ""
        texto = almacenamiento_y_uso_de_tokens.mostrar_tokens(direccion)
        listbox_frame3.listbox.delete(0, tk.END)
        for i in texto:
            if i == "\n":
                listbox_frame3.listbox.insert(tk.END, (linea))
                linea = ""
            linea += i
        listbox_frame3.listbox.insert(tk.END, (linea))

    # def mostrar_errores_sintacticos(direccion):
    #     errores = analisis_sintactico.analizar_sintaxis(direccion)
    #     listbox_frame4.listbox.delete(0, tk.END)
    #     for error in errores:
    #         listbox_frame4.listbox.insert(tk.END, error)

    # def mostrar_errores_semanticos(direccion):
    #     errores = analisis_semantico.analizar_semantica(direccion)
    #     listbox_frame5.listbox.delete(0, tk.END)
    #     for error in errores:
    #         listbox_frame5.listbox.insert(tk.END, error)

    root = tk.Tk()
    root.title("Analizador Léxico, Sintáctico y Semántico")
    root.geometry("800x600")

    # Crear un canvas para permitir el scroll
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Agregar scrollbar para el canvas
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Frame dentro del canvas para centrar el contenido
    frame_contenido = ttk.Frame(canvas)
    frame_contenido.pack(anchor="center", expand=True)  
    canvas.create_window((0, 0), window=frame_contenido, anchor="center")

    # Botón de búsqueda
    boton_busqueda = ttk.Button(frame_contenido, text="Abrir archivo", command=efectos_al_mostrar_archivo)
    boton_busqueda.pack(pady=10, padx=(100, 0))

    # Mostrar el archivo
    texto0 = ttk.Label(frame_contenido, text="Archivo:")
    texto0.pack(pady=5, padx=(100, 0))
    listbox_frame = ListboxFrame(frame_contenido)
    listbox_frame.pack(pady=5, padx=(100, 0))

    # Errores léxicos
    texto1 = ttk.Label(frame_contenido, text="Errores Léxicos:")
    texto1.pack(pady=5, padx=(100, 0))
    listbox_frame2 = ListboxFrame(frame_contenido)
    listbox_frame2.pack(pady=5, padx=(100, 0))

    #Errores sintácticos
    texto2 = ttk.Label(frame_contenido, text="Errores Sintácticos:")
    texto2.pack(pady=5, padx=(100, 0))
    listbox_frame4 = ListboxFrame(frame_contenido)
    listbox_frame4.pack(pady=5, padx=(100, 0))

    # Errores semánticos
    texto3 = ttk.Label(frame_contenido, text="Errores Semánticos:")
    texto3.pack(pady=5, padx=(100, 0))
    listbox_frame5 = ListboxFrame(frame_contenido)
    listbox_frame5.pack(pady=5, padx=(100, 0))

    # Tokens
    texto4 = ttk.Label(frame_contenido, text="Tokens:")
    texto4.pack(pady=5, padx=(100, 0))
    listbox_frame3 = ListboxFrame(frame_contenido)
    listbox_frame3.pack(pady=5, padx=(100, 0))

    root.mainloop()

main()

