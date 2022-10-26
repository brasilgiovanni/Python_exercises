#Herança de classes

class Soma_Multiplica:
	def __init__ (self, a, b):
		self.a = a
		self.b = b
	def somar(self):
		return self.a + self.b
	def multiplicar(self):
		return self.a * self.b

class Derivada(Soma_Multiplica):
	def subtrair(self):
		return self.a - self.b
	def dividir(self):
		return self.a / self.b

x = Derivada(10, 20)

print(f' A soma de 10 e 20 é = {x.somar()}')
print(f' O produto entre 10 e 20 é = {x.multiplicar()}')
print(f' A diferença entre 10 e 20 é = {x.subtrair()}')
print(f' A divisão entre 10 e 20 é = {x.dividir()}')
print('A classe Derivada é uma subclasse da Soma_Multiplica? ', issubclass(Derivada, Soma_Multiplica))

# Exemplo de "sobrecarga" de funções - tambem dito default argument
# Cuidado: SyntaxError: non-default argument follows default argument
# Ou seja, não pode ter um argumento pré-definido (subjetivo) linkado antes de argumentos que devem ser fornecidos pelo usuário

# Exemplo de erro
# def somar_numero(x, y = 0, z):
# 	return x+y+z

# valor = somar_numero(10, 20)
# print(valor)
print('---------------------------------')
# Exemplo correto
def somar_numero(x, y, z=0):
	return x+y+z

valor = somar_numero(10, 20)
print('O valor é igual a: ', valor)

print(f'O segundo valor é igual a: {somar_numero(10, 20, 30)}')

# Exemplo de Polimorfismo

class Argentina():
	def capital(self):
		print('Buenos Aires é a capital da Argentina')
	def lingua_oficial(self):
		print('O espanhol é a lingua oficial da Argentina')

class Brasil():
	def capital(self):
		print('Brasilia é a capital do Brasil')
	def lingua_oficial(self):
		print('O português é a lingua oficial do Brasil')

obj_Arg = Argentina()
obj_Bra = Brasil()

for pais in (obj_Arg, obj_Bra): # Observe que eles tem que ter os mesmos métodos (funcoes)
	print('')
	pais.capital()
	pais.lingua_oficial()

# A função super() faz referência a um método da classe "mãe"

# Mais um exemplo de Polimorfismo
print('')
class Veiculo:
	def rodar(self):
		print('Reduz o consumo de combustível.')

class VeiculoEletrico(Veiculo):
	def rodar(self):
		super().rodar()
		print('Esse veiculo utiliza eletricidade.')

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()

# Exemplo com mensagem de exceção

# x = 10
# if x > 5:
# 	raise Exception('x não pode ser maior do que 5. O valor de x foi de: {}'.format(x))

# x = 'hello'
# if not type(x) is int:
# 	raise TypeError('Use valores inteiros')

