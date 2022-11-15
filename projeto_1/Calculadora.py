from tkinter import*
from tkinter import ttk
from cores import*

janela = Tk()
janela.title("Calculadora")
janela.geometry("270x350")
janela.config(bg = cor_fundo)

frame_tela = Frame(janela, width = 270, height = 70, bg = cor_janela)
frame_tela.grid(row = 0, column = 0)

frame_body = Frame(janela, width = 270, height = 50, bg = cor_fundo)
frame_body.grid(row = 1, column = 0)

# Criando Botões

bt_C = Button(frame_body, text="C", width = 11, height = 2, bg = cor_janela)
bt_C.place(x=0, y=0)

janela.mainloop()
