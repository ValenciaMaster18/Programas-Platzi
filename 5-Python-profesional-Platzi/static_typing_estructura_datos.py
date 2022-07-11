from typing import Dict, List, Tuple

# Listas
positive: list[int] = [1, 2, 3, 4, 5]

# Diccionario
user: dict[str, int] = {
    "Argentina":7000000,
    "Colombia":50000000,
    "Brazil":1000000000
}

# Listas de diccionario
countries: list[dict[str, str]] =[
    {"Brazil":"Rio de janeiro"},
    {"Colombia":"Bogota"},
    {"Argentina":"Buenos aires"}
]

# Tuplas
num: Tuple[int, float, int]=(1, 1.5, 2)

# Listas de diccionarios con valores de tuplas

tablas: list[dict[int:tuple][int]] = [
    {1:(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)},
    {2:(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)},
    {3:(3, 6, 9, 12, 15, 18, 21, 24, 27, 30)},
    {4:(4, 8, 12, 16, 20, 24, 28, 32, 36, 40)},
    {5:(5, 10, 15, 20, 25, 30, 35, 40, 45, 50 )}
]
