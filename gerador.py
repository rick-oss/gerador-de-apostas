from random import sample, randint, shuffle


# soluçao sample
def gerador_1():
    # gera 20 números não repetidos entre 1 e 100
    gerador = sample(range(0, 100), 20)

    print(gerador)


# soluçao randint
def gerador_2():
    numeros = []

    # gera e adiciona 6 números entre 1 e 60
    while len(numeros) < 6:
        gerador = randint(1, 60)

        # Garante que os números não se repitam
        if gerador not in numeros:
            numeros.append(gerador)

    print(numeros)


# soluçao shuffle
def gerador_3():
    numeros = []

    # Adiciona os números que podem ser escolhidos
    for num in range(0, 100):
        numeros.append(num)

    shuffle(numeros)  # embaralha a lista de números
    seis_numeros = numeros[:6]  # filtra os 6 primeiros números da lista

    print(seis_numeros)


gerador_1()
gerador_2()
gerador_3()
