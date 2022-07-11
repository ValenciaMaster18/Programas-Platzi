from datetime import datetime
import pytz # Este modulo nos permite trabajar con las diferentes zonas de horarios

def main():
    time = input("Ingrese la zona horaria: ")
    lugar = input("Ingrese lugar de la zona : ")  
    zona = pytz.timezone(time)
    time = datetime.now(zona)
    print(lugar + ":  " + time.strftime("%d/%m/%Y, %H/%M/%S"))  


if __name__ == "__main__":
    main()
