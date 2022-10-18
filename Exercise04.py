# função fatorial

def fatorial(n, valor = 0):
	if n < 0 or n is float():
		print(''' Desculpe, mas não aceitamos valores negativos!
	E nem valores decimais''')
		return
	while n != 0:
		if valor == 0:
			valor = n
			return fatorial(n-1, valor)
		else:
			valor = n * valor
			return fatorial(n-1, valor)
	if n == 0 and valor !=0:
		return valor
	elif n == 0 and valor == 0:
		return 1
	else:
		pass

palavra = 'True'

while palavra != 'sair':
	x = int(input("""
 Digite um número inteiro aqui entre 0 a infinito: 
		 												..................		"""))

	print('Resposta: ', fatorial(x))
	palavra = input(""" 
 digite 'sair' para encerrar ou 'ok' para continuar:
                   ....................  """)
	if palavra == 'sair':
		print('''
	Obrigado, até logo!''')