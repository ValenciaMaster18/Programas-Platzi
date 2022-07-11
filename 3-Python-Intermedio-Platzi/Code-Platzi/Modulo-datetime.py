import datetime

def run():
    fecha_actual = datetime.datetime.now()
    print (fecha_actual) # FechaActual
    print (fecha_actual.year) # Año
    print (fecha_actual.strftime("%A")) # Dia 
    print (fecha_actual.strftime("%B")) # Mes
    
    
if __name__ == "__main__":
    run()



