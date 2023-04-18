lista = []
while True:
    ref = input()
    if ref == '0':
        break
    elif ref != '':
        lista.append(ref)

for i in lista:
   if i.startswith('\u200c'):
    index = lista.index(i)
    especial = list(i)
    del especial[0]
    fixed = ''.join(especial)
    lista[index] = fixed

x = sorted(lista, key=str.casefold)

for i in x:
    print('\n' + i)
