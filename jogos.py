import forca
import adivinhacao

def escolhe_jogo():
    print("Escolha um jogo!")

    jogo = int(input("(1) Forca (2) Adivinhação "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()