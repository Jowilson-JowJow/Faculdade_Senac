import tkinter as tk

def calcular(operacao):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        # Dicionário de operações para eliminar os vários 'ifs' ou funções repetidas
        operacoes = {
            "somar": n1 + n2,
            "subtrair": n1 - n2,
            "multiplicar": n1 * n2,
            "dividir": n1 / n2 if n2 != 0 else "Erro: Divisão por zero"
        }
        
        resultado = operacoes[operacao]
        labelResult.config(text=f"Resultado: {resultado}")
    except ValueError:
        labelResult.config(text="Informe números válidos")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora by JowJow")
janela.geometry("300x400")

# Inputs
tk.Label(janela, text="Numero 1:").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Numero 2:").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

# Botões criados em loop para economizar linhas
botoes = [
    ("Somar", "somar"),
    ("Subtrair", "subtrair"),
    ("Multiplicar", "multiplicar"),
    ("Dividir", "dividir")
]

for texto, op in botoes:
    # Usamos lambda para passar o argumento da operação para a função
    tk.Button(janela, text=texto, command=lambda o=op: calcular(o)).pack(pady=2)

labelResult = tk.Label(janela, text="Resultado: ", fg="blue")
labelResult.pack(pady=10)

janela.mainloop()
