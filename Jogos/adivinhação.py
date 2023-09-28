import random

def jogar():

    print("*********************************")
    print("Bem vindo nao jogo de adivinhação")
    print("*********************************")

    numeroSecreto = random.randrange(1, 101)
    totalDeTentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nivel"))

    if nivel == 1:
        totalDeTentativas = 20
    elif nivel == 2:
        totalDeTentativas = 10
    else:
        totalDeTentativas = 5

    for rodada in range(1, totalDeTentativas+1):
        print("Tentativa {} de {}".format(rodada,totalDeTentativas))
        chute = int(input("Digite o seu número: "))
        print("Você digitou: ", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numeroSecreto
        maior   = chute > numeroSecreto
        menor   = chute < numeroSecreto

        if acertou:
            print("Você acertou e fez {}".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontosPerdidos = abs(numeroSecreto - chute) # ex: 40 - 20 = 20
            pontos = pontos - pontosPerdidos
        rodada += 1
    print("FIM DO JOGO")

if (__name__ == "__main__"):
    jogar()
