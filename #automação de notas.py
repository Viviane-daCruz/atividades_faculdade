#automação de notas

#identificação do aluno
aluno = input("Digite o nome do aluno: ")

#entrada de notas
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
nota4 = int(input())

#calcúlo da média
media = (nota1+nota2+nota3+nota4)/4

#condição para aprovação do aluno
if media>=6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#dadas as notas, mostramos a média e a situação do aluno
print(f"Olá, {aluno}, sua média é {media}, você está {situacao}.")
