class Pessoa(object):
    def __init__(self, nome, rg, cpf, idade, salario):
        self._nome = nome
        self._rg = rg
        self._cpf = cpf
        self._idade = idade
        self._salario = salario

#############         NOME        ###################
    @property
    def nome(self):
        print('get do nome')
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('set do nome', nome)
        self._nome = nome
#####################################################

###########          RG          ####################
    @property
    def rg(self, rg):
        print('get do rg', rg)
        return self._rg

    @rg.setter
    def rg(self, rg):
        print('set do rg', rg)
        self._rg = rg  
######################################################

#########           CPF         ######################
    @property
    def cpf(self):
        print('get da cpf')
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        print('set da cpf', cpf)
        self._idade = cpf
#######################################################

########         IDADE         ########################
    @property
    def idade(self):
        print('get do idade')
        return self._idade

    @idade.setter
    def salario(self, idade):
        print('set do idade', idade)
        self._salario = idade
######################################################

#######         SALÁRIO       ########################
    @property
    def salario(self):
        print('get do salario')
        return self._salario

    @salario.setter
    def salario(self, salario):
        print('set do salario', salario)
        self._salario = salario
#######################################################

pessoa = Pessoa('Maicon', 12198188, 113.95769923, 23, 2.500)
print(pessoa.__dict__) 
pessoa.nome = 'MAIK'
pessoa.rg = 12155.887
pessoa.cpf = 11395769923
pessoa.idade = 24
pessoa.salario = 25000
print(pessoa.nome)
print(pessoa.rg)
print(pessoa.cpf)
print(pessoa.idade)
print(pessoa.salario)

    

