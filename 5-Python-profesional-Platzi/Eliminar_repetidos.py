def main():
    color =[]
    colors = ["Azul","Azul","Amarillo","Rojo","Rojo","Verde","Naranja"]
    for i in colors:
        if i not in color:
            color.append(i)
    print(color)
    
    # 2 Forma
    colors = list(set(colors))


if __name__ == "__main__":
    main()