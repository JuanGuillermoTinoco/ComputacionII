from Tkinter import *
import tkFileDialog as filedialog
from PIL import Image
from PIL import ImageTk
import os

class Imagen:
    def __init__(self, ruta, imagen, etiqueta):
        self.imagen = imagen
        self.ruta = ruta
        self.etiqueta = etiqueta.split(',')+['todos']

class Proceso:
    def __init__(self):
        self.lista = []
        self.comprobar_archivo()
        self.cargar()
    def lista_imagenes(self, ruta):
        resultados=[]
        for i in os.listdir(ruta):
            if i.endswith(('.jpg', '.jpeg', '.gif')):
                resultados.append(i)
            else:
                pass
        return resultados
    def agregar_imagen(self, ruta, imagen, etiqueta):
        libreria = open(os.path.dirname(os.path.realpath(__file__))+'/libreria.txt', 'a')
        self.lista.append(Imagen(ruta, imagen, etiqueta))
        libreria.write(ruta+'%'+imagen+'%'+etiqueta+'\n')
    def comprobar_archivo(self):
        if os.path.isfile(os.path.dirname(os.path.realpath(__file__))+'/libreria.txt'):
            pass
        else:
            open(os.path.dirname(os.path.realpath(__file__))+'/libreria.txt', 'w').close()
    def cargar(self):
        libreria = open(os.path.dirname(os.path.realpath(__file__))+'/libreria.txt', 'r')
        for linea in libreria:
            linea = linea.rstrip().split('%')
            self.lista.append(Imagen(linea[0], linea[1], linea[2]))
    def buscar(self, etiqueta_buscar):
        resultados=[]
        etiqueta_buscar = [i.lower() for i in etiqueta_buscar.split(',')]
        for imagen in self.lista:
            if any(i.lower() in etiqueta_buscar for i in imagen.etiqueta):
                resultados.append(imagen)
            else:
                pass
        return resultados

class Ventana:
    def __init__(self):
        self.mi_lista = Proceso()
        self.pantalla = Tk()
        self.menu()
        self.pantalla.mainloop()
    def menu(self):
        self.pantalla.geometry('600x450')
        for cosas in self.pantalla.winfo_children():
            cosas.destroy()
        opcion1 = Frame(self.pantalla, bg='pale turquoise')
        opcion1.pack(fill=BOTH, expand=1)
        opcion2 = Frame(self.pantalla, bg='sky blue')
        opcion2.pack(fill=BOTH, expand=1)
        Label(opcion1, text='Load images', bg='pale turquoise').pack(expand=1)
        Label(opcion2, text='Search', bg='sky blue').pack(expand=1)
        Button(opcion1, bg='pale turquoise', command=self.importar).pack(expand=1)
        Button(opcion2, bg='sky blue', command=self.willy_buscador).pack(expand=1)
    def importar(self):
        ruta = filedialog.askdirectory()
        if os.path.isdir(ruta):
            for cosas in self.pantalla.winfo_children():
                cosas.destroy()
            lugar_imagenes = Frame(self.pantalla)
            lugar_imagenes.pack(fill=BOTH, expand=1, side=RIGHT)
            lugar_botones = Frame(self.pantalla)
            lugar_botones.pack(fill=BOTH, expand=1, side=LEFT)
            def siguiente(ruta, lista_imagen, etiqueta, posicion, n, cuadro):
                self.mi_lista.agregar_imagen(ruta, lista_imagen[posicion[0]], etiqueta)
                self.mostrar_imagen(cuadro, ruta, lista_imagen, posicion, n)
            posicion = [0]
            lista_imagenes = self.mi_lista.lista_imagenes(ruta)
            label_imagen = Label(lugar_imagenes)
            label_imagen.pack()
            etiqueta = Entry(lugar_botones)
            etiqueta.grid(row=0, column=1)
            Button(lugar_botones, text='Next', command=lambda: siguiente(ruta, lista_imagenes, etiqueta.get(),posicion,1,label_imagen)).grid(row=1, column=0)
            Label(lugar_botones, text='Tag: ').grid(row=0, column=0)
            self.mostrar_imagen(label_imagen, ruta, lista_imagenes, posicion, 0)
        else:
            return False
    def mostrar_imagen(self, cuadro, ruta, imagenes, posicion, n):
        if 0 <= posicion[0]+n < len(imagenes):
            try:
                imagen = Image.open(ruta + '/' + imagenes[posicion[0]+n])
                posicion[0] = posicion[0] + n
                imagen = imagen.resize((400, 400), Image.ANTIALIAS)
                imagen = ImageTk.PhotoImage(imagen)
                cuadro['image'] = imagen
                cuadro.image = imagen
            except:
                imagenes.pop(posicion[0] + n)
        else:
            self.menu()
    def willy_buscador(self):
        self.pantalla.geometry('600x600')
        for cosas in self.pantalla.winfo_children():
            cosas.destroy()
        lugar_imagenes = Frame(self.pantalla)
        lugar_imagenes.pack(fill=BOTH, expand=1, side=TOP)
        lugar_botones = Frame(self.pantalla)
        lugar_botones.pack(fill=BOTH, expand=1, side=BOTTOM)
        Label(lugar_botones, text='Tags: ').grid(row=0, column=0)
        buscar = Entry(lugar_botones)
        buscar.grid(row=0, column=1)
        Button(lugar_botones, text='Search', command=lambda: resultados(self.mi_lista.buscar(buscar.get()),lugar_imagenes)).grid(row=1, column=0)
        Button(lugar_botones, text='Menu', command=self.menu).grid(row=1, column=1)
        def resultados(lista_imagenes, cuadro):
            for cosas in cuadro.winfo_children():
                cosas.destroy()
            for n in range(len(lista_imagenes)):
                img = Image.open(lista_imagenes[n].ruta + '/' + lista_imagenes[n].imagen)
                img = img.resize((140, 150), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                label = Label(cuadro, image=img)
                label.image = img
                label.grid(row=n//4, column=n%4)

aplicacion = Ventana()