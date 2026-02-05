'''
📋 Descrição da Tarefa:
Você está criando um pequeno sistema de um jogo de aventura onde o jogador será classificado por sua experiência e,
com base em sua escolha, executará uma ação dentro do jogo.
 
🔧 O que seu programa deve fazer:
1.Pedir ao jogador quantos pontos de experiência ele tem (XP):
Menos de 100 → "Iniciante" 
Entre 100 e 500 → "Intermediário"
Mais de 500 → "Veterano"
 
Use if/elif/else para essa classificação.
 
2. Depois, o programa deve perguntar qual ação o jogador deseja executar (usar match case): 
"A" → Atacar
"D" → Defender
"F" → Fugir
 
Qualquer outra tecla → "Ação inválida"
 
Mostre uma mensagem apropriada para cada ação, como: 
"Você avançou para o ataque!"
"Você levantou o escudo!"
"Você fugiu da batalha!"
 
📝 Regras de Entrega:
Crie seu código em um arquivo .py
Faça testes com diferentes níveis de XP e ações
Envie o código por GitHub ou por sua plataforma de aulas
'''

'''#entrada de dados do jogador'''
#variasveis para armazamentar o nome e xp do jogador
player_name = input("Digite o nome do jogador: ")
player_xp = int(input(f"Quantos pontos de experiencia {player_name} possui ? "))


'''#estrutura condicional para classificar o jogador'''
#if para definir o nivel iniciante até 100 xp
if player_xp < 100:
    print(f"O jogador {player_name} é Iniciante")

#elif para definir o nivel intermediario entre 100 e 500 xp    
elif player_xp <= 500:
    print(f"O jogador {player_name} é Intermediário")

#else para definir o nivel veterano acima de 500 xp
else:
    print(f"O jogador {player_name} é Veterano")


'''#estrutura match case para definir a ação do jogador'''
#entrada de dados para a ação do jogador
action_player = input("Qual ação deseja realizar ?\n[A] Atacar\n[D] Defender\n[F] Fugir\n Vamos la: ")

#estrutura match case para definir a ação do jogador
match action_player:
    case "A" | "a" | "Atacar" | "atacar":
        print(f"{player_name} avançou para o ataque!")
    case "D" | "d" | "Defender" | "defender":
        print(f"{player_name} levantou o escudo!")
    case "F" | "f" | "Fugir" | "fugir":
        print(f"{player_name} fugiu da batalha!")
    case _:
        print("Ação inválida")
