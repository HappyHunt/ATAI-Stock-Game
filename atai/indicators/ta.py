
def sma(source, lenght) -> float:
    suma = 0.0
    for i in range(lenght):
        suma= suma + source[i]
    srednia = suma/lenght
    print(srednia)
    return srednia
