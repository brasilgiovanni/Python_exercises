# Implementar um programa Python para criar uma classe 'Veiculo' com atributos de instância "Velocidade Máxima" e "Quilometros percorridos por litro"

class Veiculo:

	def __init__(self, nome, velocidade_max, quilometro_litro):
		self.nome = nome
		self.velocidade_max = velocidade_max
		self.quilometro_litro = quilometro_litro

	def toStr(self):
		print(f'nome = {self.nome}')
		print(f'velocidade máxima = {self.velocidade_max}')
		print(f'Quilometros percorridos por litro = {self.quilometro_litro}')

modelo_carro = Veiculo('fusca', 180, 10)
modelo_carro.toStr()


# Criar uma classe filha "Onibus" que herdará todas as variáveis e métodos da classe "veiculo"
print('-----------------------')

class Onibus(Veiculo): # Não foi solicitado que se colocasse mais funcoes
	pass

onibus_escolar = Onibus('Scania', 120, 8)
onibus_escolar.toStr()

# Modificar a classe filha "Onibus" de modo que ela forneça a quantidade de 70 assentos.
print('-------------------')
class Veiculo:

	def __init__(self, nome, velocidade_max, quilometro_litro):
		self.nome = nome
		self.velocidade_max = velocidade_max
		self.quilometro_litro = quilometro_litro

	def capacidade_assentos(self, capacidade):
		print(f'A capacidade máxima de assentos do veiculo {self.nome} é {capacidade}')

	def toStr(self):
		print(f'nome = {self.nome}')
		print(f'velocidade máxima = {self.velocidade_max}')
		print(f'Quilometros percorridos por litro = {self.quilometro_litro}')

modelo_carro = Veiculo('fusca', 180, 10)
modelo_carro.toStr()
print('---------------')
class Onibus(Veiculo):
	def capacidade_assentos(self, capacidade = 70):
		return super().capacidade_assentos(capacidade=70)

onibus_escolar = Onibus('scania', 120, 8)
onibus_escolar.toStr()
onibus_escolar.capacidade_assentos()

# Criar uma classe com método classe e método estático
print('')
print('----------------------------')
from datetime import date

class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	# um método de classe para criar um objeto Pessoa através do ano de nascimento
	@classmethod
	def Ano_Nascimento(cls, nome, ano):
		return cls(nome, date.today().year - ano)
	# Observe que tem que inserir o (cls) que indica que eh uma subclasse da classe principal. Esse exemplo permite ter uma função que retorna a própria classe para exercutar. Se a pessoa utilizar direto a classe, ela tem que digitar a sua idade. Se a pessoa preferir inserir o ano de nascimento, ela deve chamar a funcao Ano_Nascimento, que vai retornar a classe ja calculando a idade da pessoa.

	@staticmethod
	def EhMaiorIdade(idade):
		return idade >= 18

	# O método estático é para criar uma função independente da classe. Assim a pessoa pode chamar diretamente essa função e inserir os valores dos argumentos (Variáveis da funcao). Neste caso, não é necessário criar um objeto pessoa, basta apenas chamar a funcao e verificar se uma idade é maior ou igual a 18... 
	# Assim, podemos criar varias funcoes independentes dos argumentos da classe.

pessoa01 = Pessoa('Maria', 26) # aqui foi criado o objeto Maria com idade de 26 anos
pessoa02 = Pessoa.Ano_Nascimento('Ana', 2001) # aqui foi criado o objeto Ana que nasceu em 2001 e será calculado sua idade.
Maior_idade = Pessoa.EhMaiorIdade(17) # aqui estou chamando a funcao estática que existe na classe Pessoa, para conferir se o número 17 é maior ou igual a 18. Se sim, vai retornar True, senao, False.and
print(pessoa01) # apenas vai indicar que de fato é um objeto
print(pessoa01.nome) # vai informar o nome da pessoa01
print(pessoa02.idade) # vai informar a idade da pessoa02
# print(pessoa02.ano) # veja que não é possível saber o ano de nascimento da pessoa 02, uma vez que ela mesma forneceu esse dado, mas em nenhum local da classe ficou salvo.
print(Maior_idade)