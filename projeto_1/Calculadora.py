from tkinter import*
from tkinter import ttk
from cores import*

janela = Tk()
janela.title("Calculadora")
janela.geometry("277x318")
janela.config(bg = branco)
janela.resizable(width=False, height=False)

frame_tela = Frame(janela, width = 277, height = 60, bg = branco)
frame_tela.grid(row = 0, column = 0)

frame_body = Frame(janela, width = 277, height = 330, bg = rosa)
frame_body.grid(row = 1, column = 0)



# Criando Botões

bt_1 = Button(frame_body, text="C", width = 9, height = 1, bg = cinza, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_1.place(x=3, y=2)
bt_2 = Button(frame_body, text="%", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_2.place(x=141, y=2)
bt_3 = Button(frame_body, text="/", width = 4, height = 1, bg = verde, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_3.place(x=209, y=2)

#Botões 2 linha
bt_4 = Button(frame_body, text="7", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_4.place(x=3, y=53)
bt_5 = Button(frame_body, text="8", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_5.place(x=72, y=53)
bt_6 = Button(frame_body, text="9", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_6.place(x=140, y=53)
bt_7 = Button(frame_body, text="*", width =4, height = 1, bg = verde, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_7.place(x=208, y=53)

#Botões 3 linha
bt_4 = Button(frame_body, text="4", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_4.place(x=3, y=105)
bt_5 = Button(frame_body, text="5", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_5.place(x=72, y=105)
bt_6 = Button(frame_body, text="6", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_6.place(x=140, y=105)
bt_7 = Button(frame_body, text="-", width =4, height = 1, bg = verde, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_7.place(x=208, y=105)

#Botões 4 linha
bt_4 = Button(frame_body, text="1", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_4.place(x=3, y=157)
bt_5 = Button(frame_body, text="2", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_5.place(x=72, y=157)
bt_6 = Button(frame_body, text="3", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_6.place(x=140, y=157)
bt_7 = Button(frame_body, text="+", width =4, height = 1, bg = verde, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_7.place(x=208, y=157)

#Botões 5 linha
bt_8 = Button(frame_body, text="0", width = 9, height = 0, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_8.place(x=3, y=210)
bt_9 = Button(frame_body, text=".", width = 4, height = 0, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_9.place(x=141, y=210)
bt_10 = Button(frame_body, text="=", width =4, height = 0, bg = verde, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_10.place(x=208, y=210)




janela.mainloop()
