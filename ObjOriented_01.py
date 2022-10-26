# A programação orientada a objetos:
	# CLASSE:
		# QUE ENGLOBA ATRIBUTOS E MÉTODOS
		# OS ATRIBUTOS PODEM SER ENTENDIDOS COMO AS VARIÁVEIS DE PROJETO
		# JÁ OS MÉTODOS PODEMOS SER ENTENDIDOS COMO AS FUNÇÕES QUE VÃO MANIPULAR ESSAS VARIÁVEIS

# PROPRIEDADES
	# 1. Abstração: Modelo reduzido
	# 2. Encapsulamento: Restringe o acesso à métodos e atributos em uma classe. Em Python, isso é obtido usando métodos ou atributos privados, aplicando um sublinhado como prefixo (_) simples ou (__) duplo.__doc__
	# 3. Herança: permite definir uma classe que herda todos os métodos e atributos de outra classe
	# 4. Polimorfismo: Permite usar uma única interface com diferentes formas.

# EXEMPLO DE CLASSE

class Pessoa:
	def __init__(self, nome, endereco):
		self.set_nome(nome)
		self.set_endereco(endereco)

	def set_nome(self, nome):
		self.nome = nome

	def set_endereco(self, endereco):
		self.endereco = endereco

	def get_nome(self):
		return self.nome

	def get_endereco(self):
		return self.endereco

# Objeto pessoa

pessoa01 = Pessoa('maria', 'rua 01234')
pessoa02 = Pessoa('Joao', 'rua 43210')

#imprimir cada um dos objetos

print(f'Nome: {pessoa01.get_nome()}, Endereço: {pessoa01.get_endereco()}')
print('')
print(f'Nome: {pessoa02.get_nome()}, Endereço: {pessoa02.get_endereco()}')
