import tkinter as tk
import busqueda_del_archivo
import deteccion_de_errores
import almacenamiento_y_uso_de_tokens
from tkinter import ttk


def main():
    class ListboxFrame(ttk.Frame):

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
            self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
            self.listbox = tk.Listbox(
                self,
                height= 10,
                width= 100,
                xscrollcommand=self.hscrollbar.set,
                yscrollcommand=self.vscrollbar.set
            )

            self.hscrollbar.config(command=self.listbox.xview)
            self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            self.vscrollbar.config(command=self.listbox.yview)
            self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.listbox.pack()




    def efectos_al_mostrar_archivo():
        mostrar_archivo()
        mostrar_deteccion_de_error()
        mostrar_tokens()

    def mostrar_archivo():
        linea = ""
        direccion = busqueda_del_archivo.mostrar_archivo()
        listbox_frame.listbox.delete(0, tk.END)
        with open(direccion, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            for i in contenido:
                if i == "\n":
                    listbox_frame.listbox.insert(tk.END, (linea))
                    linea = ""
                linea += i
            listbox_frame.listbox.insert(tk.END, (linea))
    
    def mostrar_deteccion_de_error():
        linea = ""
        texto = deteccion_de_errores.mostrar_errores()
        listbox_frame2.listbox.delete(0, tk.END)
        for i in texto:
            if i == "\n":
                listbox_frame2.listbox.insert(tk.END, (linea))
                linea = ""
            linea += i
        listbox_frame2.listbox.insert(tk.END, (linea))

    def mostrar_tokens():
        linea = ""
        texto = almacenamiento_y_uso_de_tokens.mostrar_tokens()
        listbox_frame3.listbox.delete(0, tk.END)
        for i in texto:
            if i == "\n":
                listbox_frame3.listbox.insert(tk.END, (linea))
                linea = ""
            linea += i
        listbox_frame3.listbox.insert(tk.END, (linea))
    
    
    root = tk.Tk()
    root.title("Lista con barras de desplazamiento")
    root.geometry("700x600")

    boton_busqueda = ttk.Button(root, text = "Abrir archivo", command=efectos_al_mostrar_archivo)
    boton_busqueda.pack()

    texto0 = ttk.Label(root, text = "Archivo:")
    texto0.pack()

    listbox_frame = ListboxFrame()
    listbox_frame.pack()

    texto1 = ttk.Label(root, text = "Errores:")
    texto1.pack()

    listbox_frame2 = ListboxFrame()
    listbox_frame2.pack()
    
    texto2 = ttk.Label(root, text="Tokens")
    texto2.pack()

    listbox_frame3 = ListboxFrame()
    listbox_frame3.pack()
    root.mainloop()

main()


