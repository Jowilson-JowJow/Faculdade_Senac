import tkinter as tk
 
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("600x400")
 
 
 
def calculo():
    try:
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        operacao = EntradaOperacao.get()
 
        if operacao == "+":
            calcular = valor1 + valor2
        elif operacao == "-":
            calcular = valor1 - valor2
        elif operacao == "*":
           calcular = valor1 * valor2
        elif operacao == "/":
            calcular = valor1 / valor2
 
        result.config(text=f"Resultado: {calcular}")
    except:
        result.config(text=f"Informe Numeros Validos")
   
 
 
num1 = tk.Label(janela, text="Inserir Variável: ")
num1.pack()
entrada1 = tk.Entry(janela)
entrada1.pack()
 
 
Labeloperacao = tk.Label(janela,text="Informe a operação: ")
Labeloperacao.pack()
EntradaOperacao = tk.Entry(janela)
EntradaOperacao.pack()
 
num2 = tk.Label(janela, text="Inserir Variável: ")
num2.pack()
entrada2 = tk.Entry(janela)
entrada2.pack()
 
 
result = tk.Label(janela, text="Resultado: ")
result.pack()
 
 
botao = tk.Button(janela,text="Calcular", command=calculo)
botao.pack()
 
 
janela.mainloop()
 