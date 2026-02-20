import tkinter as tk #tras os componentes para desenhar a tela no python

numero = 0

def lerNome():
    global numero
    numero +=1
    labelResult.config(text=f'{numero}') # escrevendo em label
    inputNome.delete(0, tk.END) #escrevendo no inputtext
    inputNome.insert(0, numero)




janela = tk.Tk()#criação da janela principal
janela.title("Minha janela principal")# titulo da janela
janela.geometry("600x400")

labelNome = tk.Label(janela, text="Contador")
labelNome.pack()

inputNome = tk.Entry(janela)
inputNome.pack()

labelResult = tk.Label(janela, text="Resultado")
labelResult.pack()

botao = tk.Button(janela, text="ler", command=lerNome)
botao.pack()




janela.mainloop()#looping que mantem a janela aberta -- sempre a ultima linha do codigo'