import tkinter as tk

def somar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        soma = n1 + n2
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text="Informe números válidos")

def subtrair():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        subtracao = n1 - n2
        labelResult.config(text=f"Resultado: {subtracao}")
    except:
        labelResult.config(text="Informe números válidos")

def multiplicar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        multiplicacao = n1 * n2
        labelResult.config(text=f"Resultado: {multiplicacao}")
    except:
        labelResult.config(text="Informe números válidos")

def dividir():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        divisao = n1 / n2
        labelResult.config(text=f"Resultado: {divisao}")
    except:
        labelResult.config(text="Informe números válidos")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora by JowJow")
janela.geometry("300x200")

# Forçando colunas com o mesmo peso
for i in range(4):
    janela.grid_columnconfigure(i, weight=1, minsize=70)

labelNum1 = tk.Label(janela, text="Numero 1:")
labelNum1.grid(row=0, column=0)

entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1)

labelNum2 = tk.Label(janela, text="Numero 2:")
labelNum2.grid(row=1, column=0)

entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=1)

tk.Button(janela, text="Somar", command=somar).grid(row=2, column=0, sticky="ew")
tk.Button(janela, text="Subtrair", command=subtrair).grid(row=2, column=1, sticky="ew")
tk.Button(janela, text="Multiplicar", command=multiplicar).grid(row=2, column=2, sticky="ew")
tk.Button(janela, text="Dividir", command=dividir).grid(row=2, column=3, sticky="ew")

labelResult = tk.Label(janela, text="Resultado:")
labelResult.grid(row=3, column=0, columnspan=4)

janela.mainloop()