# Estruturas de Repetição

# While and For

	# Instrução Break
		## Essa instrução interrompa as intruções de laços

	#  Instrução Continue
		## Essa instrução interrompe apenas a intrução corrente, fazendo com que o laço passe para a próxima interação

	# Instrução Pass
		## Essa instrução atua sobre as condicionais (if). Ela pula todas as demais instruções seguintes.

# Exemplos
# 1. BREAK
while True:
	print('Ola, o jogo de palavras começou. Digite "sair" para encerrar.')
	print('')
	palavra = input ('Entre com uma palavra: \n')
	if palavra == 'sair':
		break
print('Você digitou sair e agora está fora do laço')

# 2. CONTINUE
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

# 3. PASS
for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')

