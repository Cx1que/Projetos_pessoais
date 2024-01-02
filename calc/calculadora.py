# Calculadora basica com dois numeros

print("----Insira valores válidos. -----")

a = float(input("informe o primeiro número: " ))
b = float(input("informe o segundo numero: "))

operacao = input("Qual operação voce quer realizar? ")


    
def adicao(a, b):
    return a + b
   

def subtracao(a, b):
    return a - b
        

def multiplicacao(a, b):
    return a * b
    

def divisao(a, b):
    if b == 0:
        print("Impossivel dividir por 0")
    else:
        return a / b


def resto(a, b):
    return  a % b
    

if operacao == "+":
    print(adicao(a, b))

elif operacao == "-":
    print(subtracao(a, b))

elif operacao == "*":
    print(multiplicacao(a, b))

elif operacao == "%":
    print(resto(a, b))

elif operacao == "/":
    print(divisao(a, b))

else:
    print("Operação Invalida!")