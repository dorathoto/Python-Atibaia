import os
def clear(): return os.system('cls')
clear()


lista = []

print('\033c')
print('\x1bc')
print('\033[0;44mDigite 100 para sair.\033[m')

while True:
    valor =int(input('Digite um nº: '))
    if valor==100:
        break
    else:
        lista.append(valor)

lista.sort()
print(lista)
