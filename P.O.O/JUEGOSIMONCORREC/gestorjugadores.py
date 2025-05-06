import tkinter as tk
from tkinter import *
from classjugador import jugador
import json


class gestorJugador:
    __lista: list

    def __init__(self):
        self.__lista = []

    def cargar(self):
        with open("“pysimonpuntajes.json", "r") as archi:
            dato1 = json.load(archi)
            for i in dato1:
                nombre = i.get("nombre")
                puntos = i.get("puntos")
                fecha = i.get("fecha")
                hora = i.get("hora")
                nuevo_jugador = jugador(nombre, puntos, fecha, hora)
                self.__lista.append(nuevo_jugador)

    def interfaz(self):
        j = 0
        ventana4 = tk.Tk()
        ventana4.geometry("900x900")
        ventana4.title("Lista de Puntajes")
        nombretexto = tk.Label(ventana4, text="--NOMBRE--", font=(10), width=15)
        fechatexto = tk.Label(ventana4, text="--FECHA--", font=(10), width=15)
        horatexto = tk.Label(ventana4, text="--HORA--", font=(10), width=15)
        puntajetext = tk.Label(ventana4, text="--PUNTOS--", font=(10), width=15)
        nombretexto.grid(row=0, column=0)
        fechatexto.grid(row=0, column=1)
        horatexto.grid(row=0, column=2)
        puntajetext.grid(row=0, column=3)
        for i in self.__lista:
            j += 1
            nombre = i.getnombre()
            fecha = i.getfecha()
            print(fecha)
            hora = i.gethora()
            puntos = i.getpuntos()
            nombre = tk.Label(ventana4, text=nombre, font=(10), width=15)
            fecha = tk.Label(ventana4, text=fecha, font=(10), width=15)
            hora = tk.Label(ventana4, text=hora, font=(10), width=15)
            puntaje = tk.Label(ventana4, text=puntos, font=(10), width=15)
            nombre.grid(row=j, column=0,)
            fecha.grid(row=j, column=1)
            hora.grid(row=j, column=2)
            puntaje.grid(row=j, column=3)
        ventana4.mainloop()

    def mostrar(self):
        for i in self.__lista:
            i.mostrar()

    def ordenar(self):
        self.__lista.sort()
