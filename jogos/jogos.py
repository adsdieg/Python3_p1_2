import forca
import advinhacao

def escolher_jogo():
    print("**********************************")
    print("****** Escolha o seu jogo ********")
    print("**********************************")

    print("(1) forca (2) Advinhação")

    jogo = int(input("Qual o jogo: "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Advinhação")
        advinhacao.jogar()

if (__name__ == "__main__"):
    escolher_jogo()