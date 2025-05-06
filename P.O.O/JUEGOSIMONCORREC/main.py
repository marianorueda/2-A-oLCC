import tkinter as tk
from tkinter import *
from datetime import datetime
from gestorjugadores import gestorJugador
import random
import json


def volver_rojo(boton):
    boton.config(bg="#F52300")


def cambiar_rojo(boton):
    boton.config(bg="#F76457")
    ventana2.after(500, volver_rojo, boton)


def click_rojo():
    cambiar_rojo(bloquerojo)
    eleccion.append(1)
    if len(eleccion) == len(color):
        verificar()


def volver_azul(boton):
    boton.config(bg="#0800F5")


def cambiar_azul(boton):
    boton.config(bg="#57E2F7")
    ventana2.after(500, volver_azul, boton)


def click_azul():
    cambiar_azul(bloqueazul)
    eleccion.append(2)
    if len(eleccion) == len(color):
        verificar()


def volver_amarillo(boton):
    boton.config(bg="#EFF224")


def cambiar_amarillo(boton):
    boton.config(bg="#F76457")
    ventana2.after(500, volver_amarillo, boton)


def click_amarillo():
    cambiar_amarillo(bloqueamarillo)
    eleccion.append(3)
    if len(eleccion) == len(color):
        verificar()


def volver_verde(boton):
    boton.config(bg="#39F500")


def cambiar_verde(boton):
    boton.config(bg="#FADF97")
    ventana2.after(500, volver_verde, boton)


def click_verde():
    cambiar_verde(bloqueverde)
    eleccion.append(4)
    if len(eleccion) == len(color):
        verificar()


def mostrar_secuencia():
    for i, c in enumerate(color):
        if c == 1:
            ventana2.after(1000 * i, cambiar_rojo, bloquerojo)
        elif c == 2:
            ventana2.after(1000 * i, cambiar_azul, bloqueazul)
        elif c == 3:
            ventana2.after(1000 * i, cambiar_amarillo, bloqueamarillo)
        elif c == 4:
            ventana2.after(1000 * i, cambiar_verde, bloqueverde)
    ventana2.after(1000 * len(color), habilitar_boton)


def habilitar_boton():
    bloquerojo.config(command=click_rojo)
    bloqueazul.config(command=click_azul)
    bloqueamarillo.config(command=click_amarillo)
    bloqueverde.config(command=click_verde)


def deshabilitar_boton():
    bloquerojo.config(command=lambda: None)
    bloqueazul.config(command=lambda: None)
    bloqueamarillo.config(command=lambda: None)
    bloqueverde.config(command=lambda: None)


def verificar():
    global eleccion, color, i
    if eleccion == color:
        i += 1
        puntos.config(text=str(i))
        eleccion = []
        ventana2.after(1000, nueva_ronda)
    else:
        puntos.config(text="Game Over")
        deshabilitar_boton()
        ventana2.after(1500, ventana2.destroy)


def nueva_ronda():
    eleccion.clear()
    color.append(random.randint(1, 4))
    deshabilitar_boton()
    mostrar_secuencia()


def cambiar(i):
    color = []
    if i != 0:
        m = random.randint(1, 4)
        if m == 1:
            ventana2.after(1000, cambiar_rojo, bloquerojo)
            color.append(1)
        if m == 2:
            ventana2.after(1000, cambiar_azul, bloqueazul)
            color.append(2)
        if m == 3:
            ventana2.after(1000, cambiar_amarillo, bloqueamarillo)
            color.append(3)
        if m == 4:
            ventana2.after(1000, cambiar_verde, bloqueverde)
            color.append(4)
        m = i-1
        ventana2.after(1000, cambiar, m)
        i -= 1


def cerrar_ventan():
    text = nombre.get()
    jugador.append(text)
    ventana1.destroy()


def cargar_archi(jugador, punto):
    datos = []
    with open("“pysimonpuntajes.json", "r") as archi:
        dato1 = json.load(archi)
        for i in dato1:
            nombre = i.get("nombre")
            puntos = i.get("puntos")
            fecha = i.get("fecha")
            hora = i.get("hora")
            dato = {"nombre": nombre, "puntos": puntos,
                    "fecha": fecha, "hora": hora}
            datos.append(dato)
    nombre1 = jugador
    puntos1 = punto
    fecha_hora_actual = datetime.now()
    fecha = fecha_hora_actual.strftime("%Y-%m-%d")
    hora = fecha_hora_actual.strftime("%H:%M:%S")
    dato = {"nombre": nombre1, "puntos": puntos1, "fecha": fecha, "hora": hora}
    datos.append(dato)
    with open("“pysimonpuntajes.json", "w")as archi:
        json.dump(datos, archi, indent=2)


def cerrar():
    global ventana3
    ventana2.destroy()
    ventana3.destroy()


def mostrar():
    gj.cargar()
    gj.ordenar()
    ventana3.destroy()
    gj.interfaz()


def opciones():
    cargar_archi(jugador[0], i)
    global ventana3
    ventana3 = tk.Toplevel(ventana2)
    ventana3.geometry("10x100")
    verPuntaje = tk.Button(ventana3, text="ver puntaje",
                           width=10, height=1, command=mostrar)
    salir = tk.Button(ventana3, text="salir", width=10,
                      height=1, command=cerrar)
    verPuntaje.grid(row=0, column=0)
    salir.grid(row=1, column=0)
    ventana3.mainloop()


if __name__ == "__main__":
    jugador = []
    color = []
    eleccion = []
    gj = gestorJugador()
    i = 0
    ventana1 = tk.Tk()
    ventana1.geometry("400x50")
    usuario = tk.Label(ventana1, text="jugador:", font=(20))
    nombre = tk.Entry(ventana1)
    boton = tk.Button(ventana1, text="iniciar juego",
                      width=10, height=1, command=cerrar_ventan)
    usuario.grid(row=0, column=1)
    nombre.grid(row=0, column=2)
    boton.grid(row=0, column=3)
    ventana1.mainloop()

    ventana2 = tk.Tk()
    ventana2.geometry("700x700")
    nombre = tk.Label(ventana2, text=jugador[0], font=(20))
    puntos = tk.Label(ventana2, text="0", font=(20))
    configuracion = tk.Button(
        ventana2, text="opciones", width=8, height=2, command=opciones)
    bloquerojo = tk.Button(ventana2, bg="#F52300", width=30, height=20)
    bloqueazul = tk.Button(ventana2, bg="#0800F5", width=30, height=20)
    bloqueamarillo = tk.Button(ventana2, bg="#EFF224", width=30, height=20)
    bloqueverde = tk.Button(ventana2, bg="#39F500", width=30, height=20)
    nombre.grid(row=0, column=0)
    puntos.grid(row=0, column=1)
    configuracion.grid(row=0, column=2)
    bloqueverde.grid(row=1, column=0)
    bloquerojo.grid(row=1, column=1)
    bloqueamarillo.grid(row=2, column=0)
    bloqueazul.grid(row=2, column=1)
    ventana2.after(1000, nueva_ronda)
    ventana2.mainloop()
    cargar_archi(jugador[0], i)
