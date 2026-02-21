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
janela.geometry("350x200")

labelNum1 = tk.Label(janela, text="Numero 1: ")
labelNum1.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky="e") # sticky "e" (east/direita)
#labelNum1 = tk.Label(janela, text="Numero 1:").grid(row=0,column=0) -- codigo errado

entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=2, columnspan=2, padx=5, pady=10, sticky="w") # sticky "w" (west/esquerda)
# entrada1 = tk.Entry(janela).grid(row=0,column=1) -- codigo errado

labelNum2 = tk.Label(janela, text="Numero 2: ")
labelNum2.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="e")# sticky "e" (east/direita)
# labelNum2 = tk.Label(janela, text="Numero 2:").grid(row=1,column=0)  -- codigo errado

entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=2, columnspan=2, padx=5, pady=10, sticky="w")
# entrada2 = tk.Entry(janela).grid(row=1,column=1) -- codigo errado

botao_Soma = tk.Button(janela, text="Somar", width=10, command=somar).grid(row=2, column=0, padx=3, pady=10)
botao_Subtrair = tk.Button(janela, text="Subtrair", width=10, command=subtrair).grid(row=2, column=1, padx=3)
botao_mult = tk.Button(janela, text="Multiplicar", width=10, command=multiplicar).grid(row=2, column=2, padx=3)
botao_div = tk.Button(janela, text="Dividir", width=10, command=dividir).grid(row=2, column=3, padx=3)

labelResult = tk.Label(janela, text="Resposta:", font=("Arial", 10, "bold"))
labelResult.grid(row=3, column=0, pady=10)
# labelResult = tk.Label(janela, text="Resultado: ").grid(row=3,column=0) --codigo errado

janela.mainloop()#esta linha é que deixa a janela aberta sem essa linha a janela executa e fecha - esta é ultima linha do codigo

