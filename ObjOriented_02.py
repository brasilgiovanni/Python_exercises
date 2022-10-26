# Criando classes de Pessoa, Profissao, Salario.. etc

class Pessoa:
	def __init__(self, nome, idade, email):
		self.nome = nome
		self.idade = idade
		self.email = email

	def imprimir(self):
		print(self.nome, 'tem ', self.idade, ' ano(s)')
		print('e-mail: ', self.email)

	def getidade(self):
		return self.idade

	def setidade(self, idade):
		self.idade = idade

p1 = Pessoa('Ana', 25, 'ana@gmail.com')
p1.imprimir()

class Profissao(Pessoa):
	def __init__(self, nome, idade, email, profissao):
		super().__init__(nome, idade, email)
		self.profissao = profissao
	
	def imprimir(self):
		super().imprimir()
		print('\t e trabalha como ', self.profissao)

print('')
p1 = Profissao('Ana', 25, 'ana@gmail.com', 'arquiteta')
p1.imprimir()

p2 = Profissao('Joao', 30, 'joao@gmail.com', 'engenheiro')
p2.imprimir()

print('-------------------')
class Salario:
	def __init__(self, base, bonus):
		self.base = base
		self.bonus = bonus

	def salario_anual(self):
		return (self.base*12)+self.bonus

class Empregado:
	def __init__(self, nome, idade, salario):
		self.nome = nome
		self.idade = idade
		self.salario_agregado = salario

	def salario_total(self):
		return self.salario_agregado.salario_anual()

salario = Salario(10000, 700)
empregado = Empregado('Musashi', 46, salario)
print(empregado.salario_total())


print('--------------------------')

from datetime import date

class New_Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
	# Um método de classe para criar um objeto Pessoa através do ano de nascimento.
	@classmethod
	def anoNascimento(cls, nome, ano):
		return cls(nome, date.today().year - ano)
	# Método Estático: verificar se é maior de idade
	@staticmethod
	def ehMaiorIdade(idade):
		return idade >= 18


p3 = New_Pessoa('maria', 26)
print('')
p4 = New_Pessoa.anoNascimento('douglas', 2004)
print('')
print(New_Pessoa.ehMaiorIdade(17)) # Tem que retornar False
print('')
print(New_Pessoa.ehMaiorIdade(p3.idade)) # Tem que retornar True

