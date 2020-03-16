nome = input('Digite um nome:')
nome2 = ''
for t in nome.split():
    t = t.lower()
    t = t[0].upper()+t[1:]
    nome2 = nome2 + t + ''
nome2 = nome2[0:len(nome2)-1]
print(nome2)