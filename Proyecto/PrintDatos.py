from datetime import date, time, datetime


def imprimir(dias,usuarioDinero,InteresesGanados,InteresesDevengados):
    print(f"{datetime.today()}\nDinero ingresado -> {usuarioDinero}\nPlazo fijo dias -> {dias}\nIntereses ganados -> ${InteresesGanados}\nDinero total -> ${InteresesDevengados} ")
    