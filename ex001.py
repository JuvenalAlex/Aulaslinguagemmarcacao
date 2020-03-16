cadeia = input('Digite um texto:')
cout = 0
for i in range(0, len(cadeia)):
    if cadeia[i] == 'o':
        cout = cout + 1
print('o aparece', cout, "vezes")
