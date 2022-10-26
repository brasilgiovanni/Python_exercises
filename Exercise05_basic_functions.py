# Criar uma função que encontre o menor valor de uma lista

def menor_valor(lista):
	menor = 0
	for valor in lista:
		if valor < menor:
			menor = valor
	return menor

lista01 = [0, 1, 2, 3, 4, 5, 6]
lista02 = [6, 5, 4, 3, 2, 1, 0]
lista03 = [0, -1, -2, -3, -4, 10]
print(f'''Ola, os menores valores de cada lista são respectivamente:

	Lista 01 -- {lista01} = {menor_valor(lista01)} 
	Lista 02 -- {lista02} = {menor_valor(lista02)}
	Lista 03 -- {lista03} = {menor_valor(lista03)}''')

# Somar todos os números pares de uma lista

def n_par(n):
	r = (n%2 == 0)
	return r

def soma_par(lista):
	soma = 0
	for num in lista:
		if (n_par(num)):
			soma += num

	return soma

print(f''' ---------------------------------------------
Ola, aqui veremos a soma dos números pares de cada lista:

Lista 01 -- {lista01} = {soma_par(lista01)} 
Lista 02 -- {lista02} = {soma_par(lista02)}
Lista 03 -- {lista03} = {soma_par(lista03)}''')

def n_primo(n):
	n = abs(n)
	if (n<2):
		return False
	i = n // 2
	while (i>1):
		if (n % 1 == 0):
			return False
		i -= 1
	return True

def lista_primos(lista):
	lista_primos = []
	for num in lista:
		primo = n_primo(num)
		if primo:
			lista_primos.append(num)

	return lista_primos

print(f''' ---------------------------------------------
Ola, aqui veremos os números primos de cada lista:

Lista 01 -- {lista01} = {lista_primos(lista01)} 
Lista 02 -- {lista02} = {lista_primos(lista02)}
Lista 03 -- {lista03} = {lista_primos(lista03)}''')

# Apresentar uma função recursiva de contagem

def contador(num):
	if num < 0:
		print('Até logo!')
		return
	else:
		print(num,'*'*num)
		num -= 1
		return contador(num)

print('==='*20)
print('Contagem regressiva')
x = 10
contador(x)