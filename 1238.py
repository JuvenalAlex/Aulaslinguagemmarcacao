n = int(input())
for j in range(0, n):
    out = ""
    v1, v2 = input().split()
    for i in range(0, len(v1)):
        out = out + v1[i] + v2[i]
    if len(v1) < len(v2):
        out = out + v2[1:]
    else:
        out = out + v1[1:]
