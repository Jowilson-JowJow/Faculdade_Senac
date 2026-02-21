

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
janela.geometry("300x200")

labelNum1 = tk.Label(janela, text="Numero 1:").grid(row=0,column=0)
entrada1 = tk.Entry(janela).grid(row=0,column=1)

labelNum2 = tk.Label(janela, text="Numero 2:").grid(row=1,column=0)
entrada2 = tk.Entry(janela).grid(row=1,column=1)

botao = tk.Button(janela, text="Somar",command= somar).grid(row=2,column=0)

botao = tk.Button(janela, text="Subtrair",command= subtrair).grid(row=2,column=1)

botao = tk.Button(janela, text="Multiplicar",command= multiplicar).grid(row=2,column=2)

botao = tk.Button(janela, text="Dividir",command= dividir).grid(row=2,column=3)


labelResult = tk.Label(janela, text="Resultado: ").grid(row=3,column=0)





janela.mainloop()#esta linha é que deixa a janela aberta sem essa linha a janela executa e fecha - esta é ultima linha do codigo