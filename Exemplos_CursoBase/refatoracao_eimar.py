'''
Sistema de criação de mensagem, usuaário seleciona 1 e escreve uma msg, seleciona 2, casos tenha mensagem
o sistema imprime, caso não tenha o sistema imprime uma informação que não existe mensagem. A opção 3 é apenas
fechar o sistema.
'''
import os.path

print("=============================")
print("     Sistema de Mensagem     ")
print("=============================")
print("Escolha a opção:")
print("1 - Escrever uma mensagem")
print("2 - Ler a mensagem")
print("3 - Sair do sistema.")
opcao = int(input("Informe a opção: "))

if opcao == 1:
    arquivo = open('mensagem.txt', 'w')
    msg = str(input('Digite a mensagem: '))
    arquivo.write(msg)
elif opcao == 2 and os.path.exists('mensagem.txt'):
    arquivo = open('mensagem.txt')
    texto = arquivo.readline()
    print(texto)
elif opcao == 2:
    print("Mensagem inexistente.")
else:
    exit()