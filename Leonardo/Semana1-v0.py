# Exemplo de programa no modo de edição
# Semana 1 - 001

nome = 'Leonardo'
idade = 38
altura = 1.80015       #float, pois tem casa decimais

print('==================================================')
print("O valor de nome é: ", nome)
print("O endereço da var nome na memória ram é: ", id(nome))
print("O tipo de variável para idade é:", type(idade))
print("O tipo de variável para altura é:", type(altura))
print("A idade de leonardo (%i) é maior que 40? " %idade, idade > 40)
print("Exibir altura (", altura ,"m) agora com 2 casas decimais (%.2fm)" %altura)

n1 = 1
n2 = 200

n1, n2 = n2, n1
print("N2 é maior que N1? ", n2 > n1)


