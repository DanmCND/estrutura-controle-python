'''
Você foi contratado para criar um menu interativo de atendimento para uma empresa fictícia. O sistema deve exibir as opções abaixo e, de acordo com o número digitado, apresentar uma resposta:
 
Opções do menu:
[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair
 
✅ O que o programa deve fazer:
Mostrar o menu acima.
Receber a opção digitada pelo usuário.
Utilizar match case para responder com base na opção.
Exibir uma mensagem apropriada para cada caso.
Caso digite algo inválido, exibir: "Opção inválida, tente novamente!"

✅ Critérios para o desafio estar completo:
Testar diferentes entradas para verificar todas as respostas.
Enviar o link do repositório com o Código
'''

print("===Menu Interativo de Atendimento===")

print("Escolha uma das opções abaixo:")
print("[1] Falar com atendente")
print("[2] Segunda via de boleto")
print("[3] Cancelar serviço")
print("[4] Informações sobre planos")
print("[5] Sair")

option = input("Digite o número da opção desejada: ")

match option:
    case "1" | "Falar com atendente":
        print("Conectando você a uma atendente...")

    case "2" | "Segunda via de boleto":
        print("Gerando segunda via do boleto...")

    case "3" | "Cancelar serviço":
        print("insira o motivo do cancelamento do serviço...")

    case "4" | "Informações sobre planos":
        print("Nossos planos disponíveis são: Básico, Premium e Família.")

    case "5" | "Sair":
        print("obrigado por ultilizar nossos serviços.")

    case _:
        print("Opção inválida, tente novamente!")
