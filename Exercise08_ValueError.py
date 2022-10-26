def espaco():
	print('')
	print('----------------------------------------')
	print('')

# Verificar se o usuário de fato digita um número
print('testando primeira função')
def digita_num():
	try:
		x = int(input("Digite um número aqui: "))
	except ValueError:
		print("Entre apenas com números inteiros!")
		return digita_num()
	print('>>>>> Obrigado! <<<<<<')
digita_num()

espaco()
print('testando segunda função')
def digita_num01():
	while True:
		try:
			x = int(input("Digite um número aqui: "))
			print(('>>>>> Obrigado! <<<<<<'))
			break
		except ValueError:
			print("Entre apenas com números inteiros!")
	return

digita_num01()

# Verificar se a divisão entre 2 números é válida
espaco()
def dividir():
	x = float(input('Digite o primeiro número aqui: '))
	y = float(input('Digite o segundo número aqui: '))
	try:
		resultado = x / y
		print('A resposta é: ', resultado)
		print('>>>>> Obrigado! <<<<<<')
	except ZeroDivisionError:
		print('Cuidado! Divisão por zero não é válida!')
		return dividir()
	return resultado

dividir()

# EXCEÇÕES MAIS CONHECIDAS

# KeyboardInterrupt - Acontece quando o usuário pressiona Ctrl+C, que causa interrupção do código 

# OverflowError - Quando uma expressão de ponto flutuante é avaliada com um valor muito grande

# IOError - Acontece quando há falha na operação de dado de entrada ou saída

# IndexError - Quando um índice sequencial está fora do intervalo de índices válidos

# NameError - Quando se digita um identificador não atribuido (variável não declarada)

# TypeError - Quando uma operação de função é aplicada a um objeto do tipo errado

# ValueError - Quando uma operação tem o tipo correto de argumento, mas valor incorreto

# Como entrar com um número seja inteiro ou float
try:
	x = eval(input('Entre com um número: '))
	print('Obrigado!')
except:
	print('aceitamos apenas números aqui!')

# Elaborações com múltiplas exceções

# try:
# 	Bloco 01
# except Exception01:
# 	Bloco tratado para exceção 01
# except Exception02:
# 	Bloco tratado para a exceção 02
# except Exception03:
# 	Bloco tratado para a exceção 03
# ...
# else:
# 	Bloco 02 - executado caso nenhuma exceção seja levantada
# finally:
# 	Bloco 03 - executado independente do que ocorrer no código
# ... Instruções fora do "try"
