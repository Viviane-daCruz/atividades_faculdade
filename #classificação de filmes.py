#classificação de filmes

#lista de filmes
filme1 = "filme"
filme2 = "filme"
filme3 = "filme"
filme4 = "filme"
filme5 = "filme"
filmes = [filme1, filme2, filme3, filme4, filme5]

#classificação dos filmes
for filme in filmes:
    while True:
        classificacao = input(f"{filme} de 1 a 5? (ou 0 para parar): ")
        if classificacao == 0:
            print(f"{filme} interrompido.")
            break
        classificacao = int(classificacao)
        if classificacao < 1 or classificacao > 5:
            print()
        else:
            print(f"{filme} com {classificacao} estrelas.\n")
