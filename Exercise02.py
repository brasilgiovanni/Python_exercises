print("hello world!")


def NumeroMaior(x, y):
  return (max(x, y))

x = float(input("digite aqui o primeiro valor: "))
y = float(input("digite aqui o segundo valor: "))
a = NumeroMaior(x, y)
print("O número maior é: ", a)
print('==' * 20)


def TypeNumber(x):
  type = "impar"
  if a % 2 == 0:
    type = "par"
  return type


print("O número ", a, "é do tipo ", TypeNumber(a))
print('==' * 20)
def EstudanteAprovado(x):
	resultado = "Reprovado"
	if x >= 7:
		resultado = "Aprovado"
		print("Congratulations Bro, you got it!")
	else:
		print("""Sorry my friend, you lose that one.
	Try again, next time.
                         = ( """)
	return

EstudanteAprovado(a)

print('==' * 20)

def ValorCompra(x):
	Product_value = 10
	list_discount = [0, 0.10, 0.20]
	discount = list_discount[0]
	unit_value = 10
	if x <= 10:
		pass
	elif x > 20:
		discount = list_discount[-1]
	else:
		discount = list_discount[1]
	total_value = Product_value * x * (1- discount)
	print("The number of units is ", x, "and the total value is R$ ", float(total_value), "and you got a total discount of ", discount*100, "%")

ValorCompra(a)

print("""

""")
# The Range Function
print("Hey folks, lets go create lists of numbers with the 'Range Function'! ")

def SimpleRange(x):
	simple_list = list(range(x))
	print('==='*20)
	print('Here is the Simple Range')
	print('')
	print(simple_list)
	return simple_list

def MediumRange(x, y):
	medium_range = list(range(x, y))
	print('==='*20)
	print('Here is the Medium Range')
	print('')
	print(medium_range)
	return medium_range

def Range(x, y, z):
	complete_range = list(range(x, y, z))
	print('==='*20)
	print('Here is the Complete Range')
	print('')
	print(complete_range)
	return complete_range

print("pay attention, U cannot insert a zero number in 'Z and Y' variables")
x = int(input('insert the number X: '))
y = int(input('insert the number Y: '))
z = int(input('insert the number Z: '))

list_01 = SimpleRange(x)
list_02 = MediumRange(x, y)
list_03 = Range(x, y, z)

def loopingFor(list):
	for item in list:
		print(item, "*"*item)
print('')
print('Here is my new design based on range list')
print('')
loopingFor(list_03)

print("analisando sistema")
