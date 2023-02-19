from imaplib import Int2AP
from tkinter.tix import InputOnly
from Plazo_fijo import ingresoDeDatos
from PrintDatos import imprimir
def main():
    continuar = True
    while continuar:
        print("Bienvenido!")
        dias,usuarioDinero,interesesAdevengar,interesesDevengado = ingresoDeDatos()
        imprimir(dias,usuarioDinero,interesesAdevengar,interesesDevengado)
        continuar = input("Desea continuar?\n Y/N ->")
        if continuar.upper() == "Y":
            None
        else:
            continuar = False
    








main()