nalunos = int(input("Digite o numero de alunos:"))
acc = 0
for i in range(0, nalunos):
    print('Digite a nota do alunos:', i)
    nota = int(input())
    acc = acc+nota
media = acc//nalunos
print('a media da sala é', media)