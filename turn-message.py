'''
Voce foi contratado para criar um menu interativo de mensagens de cumprimento.

Se o usuario entrar com a leta M ou a palavra "Manhã", o programa deve exibir "Bom dia! eo nome da pessoa!".
Se o usuario entrar com a letra T ou a palavra "Tarde", o programa deve exibir "Boa tarde! eo nome da pessoa!".
Se o usuario entrar com a letra N ou a palavra "Noite", o programa deve exibir "Boa noite! eo nome da pessoa!".
Se o usuario entrar com qualquer outra coisa, o programa deve exibir "Entrada inválida, por favor tente novamente!".


'''

import time


print("===Menu de Mensagens de Cumprimento===")

name = input("Por favor, insira seu nome: ")
daytime = input("Digite o período do dia:")

match daytime:
    case "M" | "m"| "Manhã" | "manhã" | "Manha" | "manha":
        print("Bom dia,", name + "!")
    
    case "T"  | "t" | "Tarde" | "tarde":
        print("Boa tarde,", name + "!")

    case "N" | "n" | "Noite" | "noite":
        print("Boa noite,", name + "!")
    
    case _:
        print("Entrada inválida, por favor tente novamente!")
