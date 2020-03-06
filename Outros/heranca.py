class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrarNome(self):
        print(self.nome)

    def mostrarIdade(self):
        print(self.idade)

# herda de pessoa, mas tem RA a mnais
class Estudante(Pessoa):
    def __init__(self, nome, idade, ra):
        # chamar o construtor da classe base, para enviar os argumentos obrigatórios
        Pessoa.__init__(self, nome, idade)
        self.ra = ra

    def StatusFacul(self):
        print("O aluno %s, %i idade, %i está reprovado" % (self.nome, self.idade, self.ra))


p1 = Pessoa('Zeca',38)
p1.mostrarNome()
print('------------------')
aluno1 = Estudante('Leo2', 39, 11223344)
aluno1.mostrarNome()
aluno1.mostrarIdade()
aluno1.StatusFacul()
