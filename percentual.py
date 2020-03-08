votos_sim=42572654	
votos_nao=43132495
percentual=100*votos_sim/(votos_sim+votos_nao)
texto='percentual{:20}de votosSIM{:20.2f}'.format(votos_sim,percentual)
print(texto)
