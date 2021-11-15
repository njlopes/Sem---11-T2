n1 = int(input().strip())
n2 = int(input().strip())
lista =[]
divisores =[]
for i in range(n1, n2+1): 
    for j in range(1, i+1):
        if i >= j:
            if i % j == 0:
                divisores.append(j)
    if len(divisores) == 2:
        lista.append(i)
    divisores = []

print(*lista, sep='''
''')
