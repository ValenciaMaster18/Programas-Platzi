from datetime import datetime


def main():
    hora = datetime.now()
    print(hora)
    
    latam = hora.strftime("%d/%m/%Y")
    print(f"Formato Latam: {latam}")
    
    usa = hora.strftime("%m/%d/%Y")
    print(f"Formato USA: {usa}")
    
    random = hora.strftime("Estamos en el year %Y")
    print(f"Formato random: {random}")

if __name__ == "__main__":
    main()