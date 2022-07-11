def make_repeater(numero):
    """_summary_
        El programa trata de multiplicar el str dependiendo el numero ingresado:
        "Luis" si ingreso el 2 ->LuisLuis
    """
    def repeater(string):
        assert isinstance(string, str), "Solo puede utilizar cadenas"
        return string * numero
    return repeater

def main():
    repeat = make_repeater (3)
    print(repeat("Luis"))



if __name__ == "__main__":
    main()
