udt = int(input())
for i in range(udt):
    num = input()
    if len(num) > 3:
        print(3)
    else:
        soma = 0
        if num[0:1] == 'o':
            soma += 1
        if num[1:2] == 'n':
            soma += 1
        if num[2:3] == 'e':
            soma += 1
        if soma >= 2:
            print(1)
        else:
             print(2)
