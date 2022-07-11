import datetime

def main():
    
    time_actual = datetime.datetime.now()
    print(time_actual)
    
    fecha_actual = datetime.date.today()
    print(fecha_actual)
    
    print(f"Dia: {fecha_actual.day}")
    print(f"Año: {fecha_actual.month}")
    print(f"Año: {fecha_actual.year}")
    
    
if __name__ == "__main__":
    main() 