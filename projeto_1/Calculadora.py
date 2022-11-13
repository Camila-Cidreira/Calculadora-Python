from tkinter import*
from tkinter import ttk
from cores import*

janela = Tk()
janela.title("Calculadora")
janela.geometry("270x350")
janela.config(bg = cor_fundo)

frame_tela = Frame(janela, width = 270, height = 50, bg = cor_janela)
frame_tela.grid(row = 0, column = 0)

frame_body = Frame(janela, width = 270, height = 10)
frame_body.grid(row = 1, column = 0)

janela.mainloop()
