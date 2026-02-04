'''
Docstring for control-structure

Calculadora simples

Precisa de valores para realizar as operações
1º Etapa Entrada:
1. O usuario deve informar dois números ou mais para realizar as operações
2. O usuario deve informar a operação desejada: soma, subtração, multiplicação ou divisão

2º Etapa Processamento:
1. O programa deve receber os números e a operação desejada
2. O programa deve realizar a operação desejada com os números informados

3º Etapa Saída:
1. O programa deve exibir o resultado da operação realizada

'''
print("===Calculadora do Kaique===")

first_number = float(input("Digite o primeiro número: "))
second_number = float(input("Digite o segundo número: "))

operation = input("Digite a operação desejada: ")

match operation:
    case "+":
        result = first_number + second_number
        print("O resultado da soma é:", result)

    case "-":
        result = first_number - second_number    
        print("O resultado da subtração é:", result)

    case "*":
        result = first_number * second_number    
        print("O resultado da multiplicação é:", result)

    case "/":
        if second_number != 0:
            result = first_number / second_number    
            print("O resultado da divisão é:", result)
        else:
            print("Erro: Divisão por zero não é permitida.")

    case _:            
        print("Operação inválida.")