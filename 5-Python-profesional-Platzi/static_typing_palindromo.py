def is_palindromo(string:str) ->bool:
    string = string.replace(" ","").lower()
    return string == string [::-1]
    


def run():
    print(is_palindromo(1000))


if __name__ == "__main__":
    run()