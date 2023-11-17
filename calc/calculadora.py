# Calculadora basica com dois numeros

print("----Insira valores válidos. -----")

a = float(input("informe o primeiro número: " ))
b = float(input("informe o segundo numero: "))

operacao = input("Qual operação voce quer realizar? ")

class Calculadora:    
    
    def adicao(self, a, b):
        resultado = a + b
        print(resultado)

    def subtracao(self, a, b):
        resultado = a - b
        print(resultado)

    def multiplicacao(self, a, b):
        resultado = a * b
        print(resultado)

    def divisao(self, a, b):
        resultado = a / b
        print(resultado)

    def resto(self, a, b):
        resultado = a % b
        print(resultado)


calc = Calculadora()

if operacao == "+":
    calc.adicao(a, b)

elif operacao == "-":
    calc.subtracao(a, b)

elif operacao == "*":
    calc.multiplicacao(a, b)

elif operacao == "%":
    calc.resto(a, b)

elif operacao == "/":
    calc.divisao(a, b)

else:
    print("Operação Invalida!")