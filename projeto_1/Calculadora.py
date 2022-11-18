from tkinter import*
from tkinter import ttk
from cores import*

janela = Tk()
janela.title("Calculadora")
janela.geometry("277x318")
janela.config(bg = branco)
janela.resizable(width= False, height=False)

frame_tela = Frame(janela, width = 277, height = 60, bg = rosa_2)
frame_tela.grid(row = 0, column = 0)

frame_body = Frame(janela, width = 277, height = 330, bg = rosa_2)
frame_body.grid(row = 1, column = 0)


valores = " "

def input_valores(event):
    
    global valores

    valores += str(event)
    valor_texto.set(valores)

def calcular():

    global valores

    resultado = eval(valores)
    valor_texto.set(resultado)

def clean_frame():

    global valores

    valores = ""
    valor_texto.set("")

#Label

valor_texto = StringVar()

label = Label(frame_tela, width = 19, height = 3, padx = 7, relief = FLAT, 
anchor="e", justify = RIGHT, font = ("Verdana 0 bold"), textvariable = valor_texto,
fg = rosa
)
label.place(x = 0, y = 0)



# Criando Botões

bt_1 = Button(frame_body, command = clean_frame, text="C", width = 9, height = 1, bg = verde, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_1.place(x=3, y=2)
bt_2 = Button(frame_body, command = lambda: input_valores("%"), text="%", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_2.place(x=141, y=2)
bt_3 = Button(frame_body, command = lambda: input_valores("/"), text="/", width = 4, height = 1, bg = rosa, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_3.place(x=209, y=2)

#Botões 2 linha
bt_4 = Button(frame_body, command = lambda: input_valores("7"), text="7", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_4.place(x=3, y=53)
bt_5 = Button(frame_body, command = lambda: input_valores("8"), text="8", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_5.place(x=72, y=53)
bt_6 = Button(frame_body, command = lambda: input_valores("9"), text="9", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_6.place(x=140, y=53)
bt_7 = Button(frame_body, command = lambda: input_valores("*"), text="*", width =4, height = 1, bg = rosa, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_7.place(x=208, y=53)

#Botões 3 linha
bt_4 = Button(frame_body, command = lambda: input_valores("4"), text="4", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_4.place(x=3, y=105)
bt_5 = Button(frame_body, command = lambda: input_valores("5"), text="5", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_5.place(x=72, y=105)
bt_6 = Button(frame_body, command = lambda: input_valores("6"), text="6", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_6.place(x=140, y=105)
bt_7 = Button(frame_body, command = lambda: input_valores("-"), text="-", width =4, height = 1, bg = rosa, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_7.place(x=208, y=105)

#Botões 4 linha
bt_4 = Button(frame_body, command = lambda: input_valores("1"), text="1", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_4.place(x=3, y=157)
bt_5 = Button(frame_body, command = lambda: input_valores("2"), text="2", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_5.place(x=72, y=157)
bt_6 = Button(frame_body, command = lambda: input_valores("3"), text="3", width = 4, height = 1, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_6.place(x=140, y=157)
bt_7 = Button(frame_body, command = lambda: input_valores("+"), text="+", width =4, height = 1, bg = rosa, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_7.place(x=208, y=157)

#Botões 5 linha
bt_8 = Button(frame_body, command = lambda: input_valores("0"), text="0", width = 9, height = 0, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_8.place(x=3, y=210)
bt_9 = Button(frame_body, command = lambda: input_valores("."), text=".", width = 4, height = 0, bg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_9.place(x=141, y=210)
bt_10 = Button(frame_body, command = calcular, text="=", width = 4, height = 0, bg = rosa, fg = branco, font = ("Verdana 0 bold"), relief = RAISED, overrelief= RIDGE)
bt_10.place(x=208, y=210)




janela.mainloop()
