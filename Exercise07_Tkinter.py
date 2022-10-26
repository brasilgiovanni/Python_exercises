from tkinter import *

JanelaPrincipal = Tk()


texto = Label(master = JanelaPrincipal, text = 'Minha Janela exibida!')
texto.place(x = 40, y = 90)


def funcClicar():
	print('Botão Pressionado')

texto.pack()

# pic = PhotoImage(file = 'Imagem01.gif') - Teria que ter uma imagem baixada na mesma pasta do arquivo do código.

botao = Button(master = JanelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

JanelaPrincipal.mainloop()