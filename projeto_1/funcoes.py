def soma(num1: float, num2: float) -> float:
    " Esta função cálcula a soma de 2 números aleatórios e retorna a soma deles"
    return num1 + num2

def subtracao(num1: float, num2: float) -> float:
    "Esta função calcula a subtração de dois números aleatórios e retorna a subtração deles"
    return num1 - num2

def multiplicacao(num1: float, num2: float) -> float:
    "Esta função calcula a multiplicação entre dois números aleatórios e retorna a multiplicação deles"
    return num1 * num2

def divisao(num1: float, num2: float) -> float:
    "Esta função calcula a divisão entre dois números aleatórios e retorna a divisão deles"
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        return num1 / num2
    
def porcentagem(num1: float, num2: float) -> float:
    "Esta função calcula a porcentagem entre dois números aleatórios e retorna a porcentagem deles"
    resultado = num1 * (num2)/100
    return resultado

if __name__ == "__main__":
    print("Este é o módulo de funções do projeto calculadora")