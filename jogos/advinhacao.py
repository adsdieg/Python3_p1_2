import random

def jogar():

    print("*********************************")
    print("Bem vindo  no jogo de advinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)

    total_de_tentativas = 0

    pontos = 1000

    print("Qual p nivel de dificuldade?")
    print("(1) Facíl (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 3:
        total_de_tentativas = 5
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 1:
        total_de_tentativas = 20
    else:
        print("Nivel incorreto!")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativas {} de {} tentativas".format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você digitar seu numero entre 1 e 100:")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você Acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto")
            elif (menor):
                print("O seu chute foi menor que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("O numero secreto e: ", numero_secreto)
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
