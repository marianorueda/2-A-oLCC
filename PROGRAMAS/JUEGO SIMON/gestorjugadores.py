import tkinter as tk
from tkinter import*
from classjugador import jugador
import json
class gestorJugador:
    __lista:list
    def __init__(self):
        self.__lista=[]

    def cargar(self):
        with open("“pysimonpuntajes.json", "r") as archi:
            dato1=json.load(archi)
            for i in dato1:
                nombre=i.get("nombre")
                puntos=i.get("puntos")
                fecha=i.get("fecha")
                hora=i.get("hora")
                nuevo_jugador=jugador(nombre,puntos,fecha,hora)
                self.__lista.append(nuevo_jugador)
    def interfaz(self):
        j=0
        ventana4 = tk.Tk()
        ventana4.geometry("750x750")
        ventana4.title("Galeria de Puntajes")
        nombretext=tk.Label(ventana4, text="nombre", font=(10),width=15)
        fechatext=tk.Label(ventana4, text="fecha", font=(10),width=15)
        horatext=tk.Label(ventana4, text="hora", font=(10),width=15)
        puntajetext=tk.Label(ventana4, text="puntaje", font=(10),width=15)
        nombretext.grid(row=0,column=0)
        fechatext.grid(row=0,column=1)
        horatext.grid(row=0,column=2)
        puntajetext.grid(row=0,column=3)
        for i in self.__lista:
            j+=1
            nombre=i.getnombre()
            fecha=i.getfecha()
            print(fecha)
            hora=i.gethora()
            puntos=i.getpuntos()
            nombre=tk.Label(ventana4, text=nombre, font=(10),width=15)
            fecha=tk.Label(ventana4, text=fecha, font=(10),width=15)
            hora=tk.Label(ventana4, text=hora, font=(10),width=15)
            puntaje=tk.Label(ventana4, text=puntos, font=(10),width=15)
            nombre.grid(row=j,column=0,)
            fecha.grid(row=j,column=1)
            hora.grid(row=j,column=2)
            puntaje.grid(row=j,column=3)
        ventana4.mainloop()
    
    def Ordenar(self):
        self.__lista.sort()

    def mostrar(self):
        for i in self.__lista:
            i.mostrar()