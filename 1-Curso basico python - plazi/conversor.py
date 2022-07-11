def Conversor(moneda,cantidad):
    Valor = 0
    # De peso colombiano a dolar
    if moneda == 1:
        valor = cantidad / 0.00026
        print(f"La cantidad de pesos colombianos es ${cantidad} en dolar es == a ${valor:.0f} dolares")
    # De dolar a peso colombianos
    elif moneda ==2:
        valor = cantidad * 3905
        print(f"La cantidad de dolar es ${cantidad} en pesos colombianos es == a ${valor} pesos")
    # De dolar a euro
    elif moneda ==3:
        valor = cantidad * 0.95
        print(f"La cantidad de dolares es ${cantidad} en euro es == a ${valor:.0f} euros")
    # De euro a dolar
    elif moneda ==4:
        valor = cantidad * 1.05
        print(f"La cantidad de euro es ${cantidad} en dolar es == a ${valor:.0f} dolares")
    else:
        print ("La opcion seleccionada del menu es inecistentes")
while True:
    try:
        print("""
        Digite una opcion del menù
            1) De peso colombiano a dolar
            2) De dolar a peso colombiano
            3) De dolar a euro
            4) De euro a dolar
            """)
        moneda = int(input(" selecciona una opcion del menù: "))
        cantidad = float(input("Ingrese la cantidad de dinero que desea convertir: "))
        cantidad = round(cantidad)
        Conversor(moneda,cantidad)
        break
    except:
        print("\t*****ERROR*****")
        print("\tIngrese valores numericos")
