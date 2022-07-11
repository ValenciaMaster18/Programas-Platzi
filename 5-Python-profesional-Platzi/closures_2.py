def divisor(numero_a):
    """_summary_

    Args:
        numero_a (int): Numero a ingresar

    Returns:
        int: Este es el divisor de la division
    """
    assert isinstance(numero_a,int), "El valor tiene que ser un numero"
    assert numero_a != 0, "El numero no puede ser cero"
    def dividend(numero_b):
        """_summary_

        Args:
            numero_b (int): Numero a ingresar

        Returns:
            int: Esta funcion nos da el resultado de dividir numero_a entre numero_b
        """
        assert isinstance(numero_b,int), "El valor tiene que ser un numero"
        assert numero_a != 0, "El numero no puede ser cero"
        return numero_a // numero_b
    return dividend


def main():
    """_summary_
        Esta es la funcion en la cual se ejecuta la funcion divisor()
    """
    operation = divisor(15)
    print(operation(0))


if __name__ == "__main__":
    main()
