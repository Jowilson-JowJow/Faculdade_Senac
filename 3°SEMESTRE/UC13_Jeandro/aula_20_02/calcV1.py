import tkinter as tk

def somar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        soma = n1+n2
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe números validos")
def subtrair():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        subtracao = n1-n2
        labelResult.config(text=f"Resultado: {subtracao}")
    except:
        labelResult.config(text=f"Informe números validos")
def multiplicar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        multiplacacao = n1*n2
        labelResult.config(text=f"Resultado: {multiplacacao}")
    except:
        labelResult.config(text=f"Informe números validos")
def dividir():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        divisao = n1/n2
        labelResult.config(text=f"Resultado: {divisao}")
    except:
        labelResult.config(text=f"Informe números validos")






#criando a janela
janela = tk.Tk()
janela.title("Calculadora by JowJow")
janela.geometry("300x400")

labelNum1 = tk.Label(janela, text="Numero 1:")
labelNum1.pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

labelNum2 = tk.Label(janela, text="Numero 2:")
labelNum2.pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

botao = tk.Button(janela, text="Somar",command= somar)
botao.pack()
botao = tk.Button(janela, text="Subtrair",command= subtrair)
botao.pack()
botao = tk.Button(janela, text="Multiplicar",command= multiplicar)
botao.pack()
botao = tk.Button(janela, text="Dividir",command= dividir)
botao.pack()

labelResult = tk.Label(janela, text="Resultado: ")
labelResult.pack()




janela.mainloop()#esta linha é que deixa a janela aberta sem essa linha a janela executa e fecha - esta é ultima linha do codigo