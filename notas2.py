acc=0
nalunos=0
print('Digite a nota do aluno:', nalunos)
nota=int(input())
while(nota>=0):
    acc=acc+nota
    nalunos=nalunos+1
    print('Digite a nota do aluno:', nalunos)
    nota=int(input())
if (nalunos>0):
    media = acc//nalunos
    print('Media={:.0f}'.format(media))
else:
    print('Nao digitou nenhuma nota!')