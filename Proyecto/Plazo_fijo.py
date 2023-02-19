def ingresoDeDatos():
    usuarioTasaAnual = float(input("Ingrese la tasa anual de su banco \n-> %"))
    usuarioActivo = int(input("Ingrese el dinero \n-> $"))
    usuarioDiasAdevengar = int(input("Ingrese la cantidad de dias a dejar el plazo fijo\n->"))
    while usuarioDiasAdevengar < 30:
        usuarioDiasAdevengar = float(input("Tiene que ser mayor a 30 dias, ingrese nuevamente\n ->"))
    interesesAdevengar,interesesDevengado = calcularPlazoFijo(usuarioTasaAnual,usuarioActivo,usuarioDiasAdevengar)
    return usuarioDiasAdevengar,usuarioActivo,interesesAdevengar,interesesDevengado
def calcularPlazoFijo(tasa,dinero,dias):
    tasa = (tasa / 100)
    dineroAdevengar =  dinero * (tasa * dias / 365)
    dineroDevengado = dinero + dineroAdevengar
    return (dineroAdevengar,dineroDevengado)
