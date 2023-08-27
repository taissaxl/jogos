import random
def jogar():
    print("Jogo de Adivinhação")

    numero_secreto = random.randrange(1, 101)
    tentativas = 3
    rodadas = 1
    pontos = 1000

    print("(1) Nível fácil (2) Nível médio (3) Nível difícil")
    nivel = int(input("Escolha um nível de dificuldade: "))

    if(nivel == 1):
        tentativas = 15
    elif(nivel == 2):
        tentativas = 10
    elif(nivel == 3):
        tentativas = 5
    else:
        print("Número inválido!")

    for rodadas in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodadas, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("O número deve estar entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto")
                if (rodadas == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O número digitado é menor do que o número secreto")
                if (rodadas == tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()

