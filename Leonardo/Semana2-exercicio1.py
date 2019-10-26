'''
Exercício semana 2
'''

rendLata = 4  # m2
custoLata = 180.00
litrosLata =18


rendimento = rendLata * litrosLata

area = int(input("Qual tamanho da área a ser pintada em m2? "))
print('O rendimento por 1 lata é: %.2f m2' %rendimento)
print('Qtd de latas para pintar é.: %.1f latas.' % (area/rendimento))
print('Custo em latas é: R$ %2.f' % (custoLata * rendimento))


