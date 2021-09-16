import tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox
import sqlite3
import PIL
from PIL import ImageTk, Image






class modulo1:
    def vort(self):
        area_admin()
        self.m1.destroy()
    def initialize_lp(self):
        lp()
    def initialize_itic(self):
        itic()
    def initialize_bd(self):
        bd()


    def __init__(self):

        self.m1 = Tk()
        self.m1.geometry('500x500')
        self.m1.resizable(False, False)
        self.m1.iconbitmap("logo.ico")
        self.m1.title("Notas/Faltas - Módulo1")

        Label(self.m1, text="").grid(row=1, column=1)

        self.lp = Button(self.m1, text="Lógica \n da \n Programação")
        self.lp.configure(width=10, height=5, foreground='white', background="black",command=self.initialize_lp)
        self.lp.grid(row=3, column=10, padx=10, pady=10)

        self.bd = Button(self.m1, text="Banco\n de \nDados",command=self.initialize_bd)
        self.bd.configure(width=10, height=5, foreground='white', background="black")
        self.bd.grid(row=3, column=11, padx=10, pady=10)

        self.it = Button(self.m1, text="ITIC")
        self.it.configure(width=10, height=5, foreground='white', background="black",command=self.initialize_itic)
        self.it.grid(row=3, column=12, padx=10, pady=10)

        self.back1 = Button(self.m1, text="voltar",command=self.vort)
        self.back1.configure(width=10, height=5, foreground='white', background="black")
        self.back1.grid(row=3, column=13, padx=10, pady=10)


# Matérias-----------------------------------------------------------------------------------------------------------

class lp:
    def refresh(self):
        self.nome_entry.delete(0, "end")
        self.n1_entry.delete(0, "end")
        self.n2_entry.delete(0, "end")
        self.nfinal_entry.delete(0, "end")
        self.falta_entry.delete(0, "end")


    def new(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        cursor.execute("""INSERT INTO cad1 (nome, n1, n2, nfinal,faltas)
                           VALUES (?,?,?,?)""",
                       (self.nome_entry.get(), self.n1_entry.get(), self.n2_entry.get(), self.nfinal_entry.get()))
        auto.commit()
        self.refresh()
        for i in self.treen.get_children():
            self.treen.delete(i)
        self.view()

        messagebox.showinfo("Alerta Banco de Dados", "Cadastro realizado com sucesso")

        auto.close()

    def view(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()



        for row in rows:
            listlp = (row[0],row[4],row[5],row[6],row[7])



            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()
            self.lala = self.nome_entry.get()



            self.treen.insert("", tkinter.END, values=listlp)

            cursor.execute("""UPDATE cad1 SET n1 =?, n2 =?, nfinal =?,faltas=? WHERE nome =?""",
                               (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.lala))
            auto.commit()

        auto.commit()
        auto.close()





    def att(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.s = self.nome_entry.get()
        cursor.execute("""UPDATE cad1 SET n1 = ?, n2 =?, nfinal =?, faltas=? WHERE nome =?""",
                       (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.s))
        auto.commit()
        self.refresh()
        for i in self.treen.get_children():
            self.treen.delete(i)
        self.view()
        messagebox.showinfo("Alerta Banco de Dados", "Atualização realizada com sucesso")

        auto.close()





    def bindp(self,event):
        self.refresh()
        for n in self.treen.selection():
            column1,column2,column3,column4,column5 = self.treen.item(n,'values')
        self.nome_entry.insert(END, column1)
        self.n1_entry.insert(END, column2)
        self.n2_entry.insert(END, column3)
        self.nfinal_entry.insert(END, column4)
        self.falta_entry.insert(END, column5)








    def __init__(self):
        self.lpp = Tk()
        self.lpp.resizable(False, False)
        self.lpp.iconbitmap("logo.ico")
        self.lpp.title("Notas/Faltas - Lógica da Programação")

        # Labels----------------------------------------------------------------

        self.nome_Label = Label(self.lpp, text="Nome", font="Times")
        self.nome_Label.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.n1_Label = Label(self.lpp, text="N1", font="Times")
        self.n1_Label.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        self.n2_Label = Label(self.lpp, text="N2", font="Times")
        self.n2_Label.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.lpp, text="Média Final", font="Times")
        self.nfinal_Label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.lpp, text="Faltas", font="Times")
        self.nfinal_Label.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        # Entrys-------------------------------------------------------------------

        self.nome_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.nome_entry.grid(row=0, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n1_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.n1_entry.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n2_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.n2_entry.grid(row=2, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.nfinal_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.nfinal_entry.grid(row=3, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.falta_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.falta_entry.grid(row=4, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)


        # Buttons-----------------------------------------------------------------------------

        self.submit_button = ttk.Button(self.lpp, text="Submeter Nota",command=self.att)
        self.submit_button.grid(row=0, column=3, padx=9, sticky=W + E + S)




        # Registers----------------------------------------------------------------------


        self.treen = ttk.Treeview(self.lpp, selectmode="browse",
                                 column=("column1", "column5", "column6", "column7","column8"),
                                 show='headings')
        self.treen.column("column1", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#1", text="Nome")

        self.treen.column("column5", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#2", text="N1")

        self.treen.column("column6", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#3", text="N2")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#4", text="Média Final")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#5", text="Faltas")

        self.treen.grid(row=5, column=0, columnspan=6, padx=9, sticky=W + E)

        self.vsb = ttk.Scrollbar(self.lpp, orient="vertical", command=self.treen.yview)
        self.vsb.place(x=30+550+2, y=220, height=200+20)

        self.treen.configure(yscrollcommand=self.vsb.set)

        self.treen.bind('<Double-1>',self.bindp)


        # Search---------------------------------------------------------------------------



        Label(self.lpp, text="ETE - Jurandir Bezerra Lins").grid(row=6, column=1, sticky=E,
                                                                          padx=9, pady=9)



        self.view()
        self.lpp.mainloop()

#---------
class itic:
    def refresh(self):
        self.nome_entry.delete(0, "end")
        self.n1_entry.delete(0, "end")
        self.n2_entry.delete(0, "end")
        self.nfinal_entry.delete(0, "end")
        self.falta_entry.delete(0, "end")



    def view(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()



        for row in rows:
            listitic = (row[0],row[8],row[9],row[10],row[7])



            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()
            self.lala = self.nome_entry.get()



            self.treen.insert("", tkinter.END, values=listitic)

            cursor.execute("""UPDATE cad1 SET n1itic =?, n2itic =?, nfinalitic =?,faltas=? WHERE nome =?""",
                               (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.lala))
            auto.commit()

        auto.commit()
        auto.close()





    def att(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.s = self.nome_entry.get()
        cursor.execute("""UPDATE cad1 SET n1itic = ?, n2itic =?, nfinalitic =?, faltas=? WHERE nome =?""",
                       (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.s))
        auto.commit()
        self.refresh()
        for i in self.treen.get_children():
            self.treen.delete(i)
        self.view()
        messagebox.showinfo("Alerta Banco de Dados", "Atualização realizada com sucesso")

        auto.close()





    def bindp(self,event):
        self.refresh()
        for n in self.treen.selection():
            column1,column2,column3,column4,column5 = self.treen.item(n,'values')
        self.nome_entry.insert(END, column1)
        self.n1_entry.insert(END, column2)
        self.n2_entry.insert(END, column3)
        self.nfinal_entry.insert(END, column4)
        self.falta_entry.insert(END, column5)








    def __init__(self):
        self.lpp = Tk()
        self.lpp.resizable(False, False)
        self.lpp.iconbitmap("logo.ico")
        self.lpp.title("Notas/Faltas - Itic")

        # Labels----------------------------------------------------------------

        self.nome_Label = Label(self.lpp, text="Nome", font="Times")
        self.nome_Label.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.n1_Label = Label(self.lpp, text="N1", font="Times")
        self.n1_Label.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        self.n2_Label = Label(self.lpp, text="N2", font="Times")
        self.n2_Label.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.lpp, text="Média Final", font="Times")
        self.nfinal_Label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.lpp, text="Faltas", font="Times")
        self.nfinal_Label.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        # Entrys-------------------------------------------------------------------

        self.nome_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.nome_entry.grid(row=0, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n1_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.n1_entry.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n2_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.n2_entry.grid(row=2, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.nfinal_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.nfinal_entry.grid(row=3, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.falta_entry = ttk.Entry(self.lpp, font="Times", foreground='black')
        self.falta_entry.grid(row=4, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)


        # Buttons-----------------------------------------------------------------------------

        self.submit_button = ttk.Button(self.lpp, text="Submeter Nota",command=self.att)
        self.submit_button.grid(row=0, column=3, padx=9, sticky=W + E)




        # Registers----------------------------------------------------------------------


        self.treen = ttk.Treeview(self.lpp, selectmode="browse",
                                 column=("column1", "column5", "column6", "column7","column8"),
                                 show='headings')
        self.treen.column("column1", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#1", text="Nome")

        self.treen.column("column5", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#2", text="N1")

        self.treen.column("column6", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#3", text="N2")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#4", text="Média Final")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#5", text="Faltas")

        self.treen.grid(row=5, column=0, columnspan=6, padx=9, sticky=W + E)

        self.vsb = ttk.Scrollbar(self.lpp, orient="vertical", command=self.treen.yview)
        self.vsb.place(x=30+550+2, y=220, height=200+20)

        self.treen.configure(yscrollcommand=self.vsb.set)

        self.treen.bind('<Double-1>',self.bindp)


        # Search---------------------------------------------------------------------------



        Label(self.lpp, text="SEETE - GESTÃO ESCOLAR").grid(row=6, column=1, sticky=E,
                                                                          padx=9, pady=9)



        self.view()
        self.lpp.mainloop()

#------------------------------
class bd:
    def refresh(self):
        self.nome_entry.delete(0, "end")
        self.n1_entry.delete(0, "end")
        self.n2_entry.delete(0, "end")
        self.nfinal_entry.delete(0, "end")
        self.falta_entry.delete(0, "end")



    def view(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()



        for row in rows:
            listitic = (row[0],row[11],row[12],row[13],row[7])



            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()
            self.lala = self.nome_entry.get()



            self.treen.insert("", tkinter.END, values=listitic)

            cursor.execute("""UPDATE cad1 SET n1bd =?, n2bd =?, nfinalbd =?,faltas=? WHERE nome =?""",
                               (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.lala))
            auto.commit()

        auto.commit()
        auto.close()





    def att(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.s = self.nome_entry.get()
        cursor.execute("""UPDATE cad1 SET n1bd = ?, n2bd =?, nfinalbd =?, faltas=? WHERE nome =?""",
                       (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.s))
        auto.commit()
        self.refresh()
        for i in self.treen.get_children():
            self.treen.delete(i)
        self.view()
        messagebox.showinfo("Alerta Banco de Dados", "Atualização realizada com sucesso")

        auto.close()





    def bindp(self,event):
        self.refresh()
        for n in self.treen.selection():
            column1,column2,column3,column4,column5 = self.treen.item(n,'values')
        self.nome_entry.insert(END, column1)
        self.n1_entry.insert(END, column2)
        self.n2_entry.insert(END, column3)
        self.nfinal_entry.insert(END, column4)
        self.falta_entry.insert(END, column5)








    def __init__(self):
        self.bdd = Tk()
        self.bdd.resizable(False, False)
        self.bdd.iconbitmap("logo.ico")
        self.bdd.title("Cadastro de Alunos")

        # Labels----------------------------------------------------------------

        self.nome_Label = Label(self.bdd, text="Nome", font="Times")
        self.nome_Label.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.n1_Label = Label(self.bdd, text="N1", font="Times")
        self.n1_Label.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        self.n2_Label = Label(self.bdd, text="N2", font="Times")
        self.n2_Label.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Média Final", font="Times")
        self.nfinal_Label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Faltas", font="Times")
        self.nfinal_Label.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        # Entrys-------------------------------------------------------------------

        self.nome_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nome_entry.grid(row=0, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n1_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n1_entry.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n2_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n2_entry.grid(row=2, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.nfinal_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nfinal_entry.grid(row=3, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.falta_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.falta_entry.grid(row=4, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)


        # Buttons-----------------------------------------------------------------------------

        self.submit_button = ttk.Button(self.bdd, text="Submeter Nota",command=self.att)
        self.submit_button.grid(row=0, column=3, padx=9, sticky=W + E)




        # Registers----------------------------------------------------------------------


        self.treen = ttk.Treeview(self.bdd, selectmode="browse",
                                 column=("column1", "column5", "column6", "column7","column8"),
                                 show='headings')
        self.treen.column("column1", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#1", text="Nome")

        self.treen.column("column5", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#2", text="N1")

        self.treen.column("column6", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#3", text="N2")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#4", text="Média Final")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#5", text="Faltas")

        self.treen.grid(row=5, column=0, columnspan=6, padx=9, sticky=W + E)

        self.vsb = ttk.Scrollbar(self.bdd, orient="vertical", command=self.treen.yview)
        self.vsb.place(x=30+550+2, y=220, height=200+20)

        self.treen.configure(yscrollcommand=self.vsb.set)

        self.treen.bind('<Double-1>',self.bindp)


        # Search---------------------------------------------------------------------------



        Label(self.bdd, text="SEETE - GESTÃO ESCOLAR").grid(row=6, column=1,sticky=E,
                                                                          padx=9, pady=9)



        self.view()
        self.bdd.mainloop()



#Fim Matérias-----------------------------------------------------------------------------------------------------------------------------------


class notas_bd:
    def refresh(self):
        self.nome_entry.delete(0, "end")
        self.n1_entry.delete(0, "end")
        self.n2_entry.delete(0, "end")
        self.nfinal_entry.delete(0, "end")
        self.falta_entry.delete(0, "end")



    def view(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()



        for row in rows:
            listitic = (row[0],row[11],row[12],row[13],row[7])



            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()
            self.lala = self.nome_entry.get()

            if  validate_user == row[1]:
                self.nfinal_Label = Label(self.bdd, text=row[0], font="Times")
                self.nfinal_Label.grid(row=0, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[11], font="Times")
                self.nfinal_Label.grid(row=1, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[12], font="Times")
                self.nfinal_Label.grid(row=2, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[13], font="Times")
                self.nfinal_Label.grid(row=3, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[7], font="Times")
                self.nfinal_Label.grid(row=4, column=1, sticky=W, pady=10, padx=10)








            self.treen.insert("", tkinter.END, values=listitic)

            cursor.execute("""UPDATE cad1 SET n1bd =?, n2bd =?, nfinalbd =?,faltas=? WHERE nome =?""",
                               (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.lala))
            auto.commit()


        auto.commit()
        auto.close()





    def att(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.s = self.nome_entry.get()
        cursor.execute("""UPDATE cad1 SET n1bd = ?, n2bd =?, nfinalbd =?, faltas=? WHERE nome =?""",
                       (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.s))
        auto.commit()
        self.refresh()
        for i in self.treen.get_children():
            self.treen.delete(i)
        self.view()
        messagebox.showinfo("Alerta Banco de Dados", "Atualização realizada com sucesso")

        auto.close()





    def bindp(self,event):
        self.refresh()
        for n in self.treen.selection():
            column1,column2,column3,column4,column5 = self.treen.item(n,'values')
        self.nome_entry.insert(END, column1)
        self.n1_entry.insert(END, column2)
        self.n2_entry.insert(END, column3)
        self.nfinal_entry.insert(END, column4)
        self.falta_entry.insert(END, column5)








    def __init__(self):
        self.bdd = Tk()
        self.bdd.geometry('300x250')
        self.bdd.resizable(False, False)
        self.bdd.iconbitmap("logo.ico")
        self.bdd.title("Notas - Banco de dados")

        # Labels----------------------------------------------------------------

        self.nome_Label = Label(self.bdd, text="Nome", font="Times")
        self.nome_Label.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.n1_Label = Label(self.bdd, text="N1", font="Times")
        self.n1_Label.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        self.n2_Label = Label(self.bdd, text="N2", font="Times")
        self.n2_Label.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Média Final", font="Times")
        self.nfinal_Label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Faltas", font="Times")
        self.nfinal_Label.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        # Entrys-------------------------------------------------------------------

        self.nome_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nome_entry.grid(row=0, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n1_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n1_entry.grid(row=1, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n2_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n2_entry.grid(row=2, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.nfinal_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nfinal_entry.grid(row=3, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.falta_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.falta_entry.grid(row=4, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)







        # Registers----------------------------------------------------------------------


        self.treen = ttk.Treeview(self.bdd, selectmode="browse",
                                 column=("column1", "column5", "column6", "column7","column8"),
                                 show='headings')
        self.treen.column("column1", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#1", text="Nome")

        self.treen.column("column5", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#2", text="N1")

        self.treen.column("column6", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#3", text="N2")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#4", text="Média Final")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#5", text="Faltas")

        self.treen.grid(row=8, column=0, columnspan=6, padx=9, sticky=W + E)

        self.vsb = ttk.Scrollbar(self.bdd, orient="vertical", command=self.treen.yview)
        self.vsb.place(x=30+550+2, y=220, height=200+20)

        self.treen.configure(yscrollcommand=self.vsb.set)

        self.treen.bind('<Double-1>',self.bindp)


        # Search---------------------------------------------------------------------------



        Label(self.bdd, text="").grid(row=6, column=1, columnspan=2, sticky=E,
                                                                          padx=9, pady=9)



        self.view()
        self.bdd.mainloop()

class notas_lp:
    def refresh(self):
        self.nome_entry.delete(0, "end")
        self.n1_entry.delete(0, "end")
        self.n2_entry.delete(0, "end")
        self.nfinal_entry.delete(0, "end")
        self.falta_entry.delete(0, "end")



    def view(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()



        for row in rows:
            listitic = (row[0],row[4],row[5],row[6],row[7])



            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()
            self.lala = self.nome_entry.get()

            if  validate_user == row[1]:
                self.nfinal_Label = Label(self.bdd, text=row[0], font="Times")
                self.nfinal_Label.grid(row=0, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[4], font="Times")
                self.nfinal_Label.grid(row=1, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[5], font="Times")
                self.nfinal_Label.grid(row=2, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[6], font="Times")
                self.nfinal_Label.grid(row=3, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[7], font="Times")
                self.nfinal_Label.grid(row=4, column=1, sticky=W, pady=10, padx=10)

                print("deu certo")






            self.treen.insert("", tkinter.END, values=listitic)

            cursor.execute("""UPDATE cad1 SET n1bd =?, n2bd =?, nfinalbd =?,faltas=? WHERE nome =?""",
                               (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.lala))
            auto.commit()


        auto.commit()
        auto.close()





    def att(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.s = self.nome_entry.get()
        cursor.execute("""UPDATE cad1 SET n1bd = ?, n2bd =?, nfinalbd =?, faltas=? WHERE nome =?""",
                       (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.s))
        auto.commit()
        self.refresh()
        for i in self.treen.get_children():
            self.treen.delete(i)
        self.view()
        messagebox.showinfo("Alerta Banco de Dados", "Atualização realizada com sucesso")

        auto.close()





    def bindp(self,event):
        self.refresh()
        for n in self.treen.selection():
            column1,column2,column3,column4,column5 = self.treen.item(n,'values')
        self.nome_entry.insert(END, column1)
        self.n1_entry.insert(END, column2)
        self.n2_entry.insert(END, column3)
        self.nfinal_entry.insert(END, column4)
        self.falta_entry.insert(END, column5)








    def __init__(self):
        self.bdd = Tk()
        self.bdd.geometry('300x250')
        self.bdd.resizable(False, False)
        self.bdd.iconbitmap("logo.ico")
        self.bdd.title("Notas - Lógica da Programação")

        # Labels----------------------------------------------------------------

        self.nome_Label = Label(self.bdd, text="Nome", font="Times")
        self.nome_Label.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.n1_Label = Label(self.bdd, text="N1", font="Times")
        self.n1_Label.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        self.n2_Label = Label(self.bdd, text="N2", font="Times")
        self.n2_Label.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Média Final", font="Times")
        self.nfinal_Label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Faltas", font="Times")
        self.nfinal_Label.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        # Entrys-------------------------------------------------------------------

        self.nome_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nome_entry.grid(row=0, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n1_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n1_entry.grid(row=1, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n2_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n2_entry.grid(row=2, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.nfinal_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nfinal_entry.grid(row=3, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.falta_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.falta_entry.grid(row=4, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)







        # Registers----------------------------------------------------------------------


        self.treen = ttk.Treeview(self.bdd, selectmode="browse",
                                 column=("column1", "column5", "column6", "column7","column8"),
                                 show='headings')
        self.treen.column("column1", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#1", text="Nome")

        self.treen.column("column5", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#2", text="N1")

        self.treen.column("column6", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#3", text="N2")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#4", text="Média Final")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#5", text="Faltas")

        self.treen.grid(row=8, column=0, columnspan=6, padx=9, sticky=W + E)

        self.vsb = ttk.Scrollbar(self.bdd, orient="vertical", command=self.treen.yview)
        self.vsb.place(x=30+550+2, y=220, height=200+20)

        self.treen.configure(yscrollcommand=self.vsb.set)

        self.treen.bind('<Double-1>',self.bindp)


        # Search---------------------------------------------------------------------------



        Label(self.bdd, text="").grid(row=6, column=1, columnspan=2, sticky=E,
                                                                          padx=9, pady=9)



        self.view()
        self.bdd.mainloop()

class notas_itic:
    def refresh(self):
        self.nome_entry.delete(0, "end")
        self.n1_entry.delete(0, "end")
        self.n2_entry.delete(0, "end")
        self.nfinal_entry.delete(0, "end")
        self.falta_entry.delete(0, "end")



    def view(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()



        for row in rows:
            listitic = (row[0],row[8],row[9],row[10],row[7])



            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()
            self.lala = self.nome_entry.get()

            if  validate_user == row[1]:
                self.nfinal_Label = Label(self.bdd, text=row[0], font="Times")
                self.nfinal_Label.grid(row=0, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[8], font="Times")
                self.nfinal_Label.grid(row=1, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[9], font="Times")
                self.nfinal_Label.grid(row=2, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[10], font="Times")
                self.nfinal_Label.grid(row=3, column=1, sticky=W, pady=10, padx=10)
                self.nfinal_Label = Label(self.bdd, text=row[7], font="Times")
                self.nfinal_Label.grid(row=4, column=1, sticky=W, pady=10, padx=10)

                print("deu certo")






            self.treen.insert("", tkinter.END, values=listitic)

            cursor.execute("""UPDATE cad1 SET n1bd =?, n2bd =?, nfinalbd =?,faltas=? WHERE nome =?""",
                               (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.lala))
            auto.commit()


        auto.commit()
        auto.close()





    def att(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.s = self.nome_entry.get()
        cursor.execute("""UPDATE cad1 SET n1bd = ?, n2bd =?, nfinalbd =?, faltas=? WHERE nome =?""",
                       (self.n1_entry.get(),self.n2_entry.get(), self.nfinal_entry.get(),self.falta_entry.get(), self.s))
        auto.commit()
        self.refresh()
        for i in self.treen.get_children():
            self.treen.delete(i)
        self.view()
        messagebox.showinfo("Alerta Banco de Dados", "Atualização realizada com sucesso")

        auto.close()





    def bindp(self,event):
        self.refresh()
        for n in self.treen.selection():
            column1,column2,column3,column4,column5 = self.treen.item(n,'values')
        self.nome_entry.insert(END, column1)
        self.n1_entry.insert(END, column2)
        self.n2_entry.insert(END, column3)
        self.nfinal_entry.insert(END, column4)
        self.falta_entry.insert(END, column5)








    def __init__(self):
        self.bdd = Tk()
        self.bdd.geometry('300x250')
        self.bdd.resizable(False, False)
        self.bdd.iconbitmap("logo.ico")
        self.bdd.title("Notas - ITIC")

        # Labels----------------------------------------------------------------

        self.nome_Label = Label(self.bdd, text="Nome", font="Times")
        self.nome_Label.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.n1_Label = Label(self.bdd, text="N1", font="Times")
        self.n1_Label.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        self.n2_Label = Label(self.bdd, text="N2", font="Times")
        self.n2_Label.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Média Final", font="Times")
        self.nfinal_Label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.nfinal_Label = Label(self.bdd, text="Faltas", font="Times")
        self.nfinal_Label.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        # Entrys-------------------------------------------------------------------

        self.nome_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nome_entry.grid(row=0, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n1_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n1_entry.grid(row=1, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.n2_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.n2_entry.grid(row=2, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.nfinal_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.nfinal_entry.grid(row=3, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.falta_entry = ttk.Entry(self.bdd, font="Times", foreground='black')
        self.falta_entry.grid(row=4, column=10, columnspan=2, sticky=W + E, padx=10, pady=0)







        # Registers----------------------------------------------------------------------


        self.treen = ttk.Treeview(self.bdd, selectmode="browse",
                                 column=("column1", "column5", "column6", "column7","column8"),
                                 show='headings')
        self.treen.column("column1", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#1", text="Nome")

        self.treen.column("column5", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#2", text="N1")

        self.treen.column("column6", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#3", text="N2")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#4", text="Média Final")

        self.treen.column("column7", width=100, minwidth=100, stretch=NO)
        self.treen.heading("#5", text="Faltas")

        self.treen.grid(row=8, column=0, columnspan=6, padx=9, sticky=W + E)

        self.vsb = ttk.Scrollbar(self.bdd, orient="vertical", command=self.treen.yview)
        self.vsb.place(x=30+550+2, y=220, height=200+20)

        self.treen.configure(yscrollcommand=self.vsb.set)

        self.treen.bind('<Double-1>',self.bindp)


        # Search---------------------------------------------------------------------------



        Label(self.bdd, text="").grid(row=6, column=1, columnspan=2, sticky=E,
                                                                          padx=9, pady=9)



        self.view()
        self.bdd.mainloop()

class area_use:



    def initialize_notas_bd(self):
        notas_bd()

    def initialize_notas_itic(self):
        notas_itic()

    def initialize_notas_lp(self):
        notas_lp()


    def site_turma(self):
        import os, webbrowser
        from urllib.request import pathname2url
        url = ('https://sites.google.com/view/etejbl/subsequente?authuser=0')
        webbrowser.open(url)


    def __init__(self):

        self.user = Tk()

        self.user.resizable(False, False)
        self.user.iconbitmap("logo.ico")
        self.user.title("Área do Aluno")

        Label(self.user, text="").grid(row=1, column=1)

        self.cad = Button(self.user, text="Lógica\n da\n Programação",command=self.initialize_notas_lp)
        self.cad.configure(width=10, height=5, foreground='white', background="black")
        self.cad.grid(row=3, column=10, padx=10, pady=10)

        self.view = Button(self.user, text="ITIC",command=self.initialize_notas_itic)
        self.view.configure(width=10, height=5, foreground='white', background="black")
        self.view.grid(row=3, column=11, padx=10, pady=10)

        self.view = Button(self.user, text="Banco\n de\n Dados\n", command=self.initialize_notas_bd)
        self.view.configure(width=10, height=5,foreground='white', background="black")
        self.view.grid(row=3, column=12, padx=10, pady=10)

        #self.back2 = Button(self.user, text="Voltar",command=self.back)
        #self.back2.configure(width=5, height=2)
        #self.back2.grid(row=3, column=13, padx=10, pady=10)

        self.back2 = Button(self.user, text="Site da Turma", command=self.site_turma)
        self.back2.configure(width=20, height=2,foreground='white', background="red")
        self.back2.grid(row=4, column=5, padx=10, pady=10,columnspan=10)







class choice:



    def choice1(self):
        area_admin()
        self.choice_area.destroy()



    def __init__(self):

        self.choice_area = Tk()

        self.choice_area.resizable(False, False)
        self.choice_area.iconbitmap("logo.ico")
        self.choice_area.title("Módulos")

        Label(self.choice_area, text="").grid(row=1, column=1)

        self.cad = Button(self.choice_area, text="Módulo 1")
        self.cad.configure(width=10, height=5, foreground='white', background="black",command=self.choice1)
        self.cad.grid(row=3, column=10, padx=10, pady=10)

        self.view = Button(self.choice_area, text="Módulo 2")
        self.view.configure(width=10, height=5, foreground='white', background="black")
        self.view.grid(row=3, column=11, padx=10, pady=10)

        self.view = Button(self.choice_area, text="Módulo 3")
        self.view.configure(width=10, height=5,state=DISABLED)
        self.view.grid(row=3, column=12, padx=10, pady=10)




class area_admin:

    def logger(self):
        admin_log()

    def voltar(self):
        choice()
        self.admin_area.destroy()


    def lognot(self):

        modulo1()
        self.admin_area.destroy()

    def __init__(self):
        self.tree = None
        self.admin_area = Tk()

        self.admin_area.resizable(False, False)
        self.admin_area.iconbitmap("logo.ico")
        self.admin_area.title("Área do Professor")

        Label(self.admin_area, text="").grid(row=1, column=1)

        self.cad = Button(self.admin_area, text="Gerenciamento \n de \n Cadastros", command=self.logger)
        self.cad.configure(width=12, height=5, foreground='white', background="black")
        self.cad.grid(row=3, column=10, padx=10, pady=10)

        self.view = Button(self.admin_area, text="Notas/Faltas")
        self.view.configure(width=12, height=5, foreground='white', background="black", command=self.lognot)
        self.view.grid(row=3, column=11, padx=10, pady=10)




        self.back = Button(self.admin_area,text="Voltar")
        self.back.configure(width=5, height=2, command=self.voltar)
        self.back.grid(row=3, column=14, padx=10, pady=10)

        Label(self.admin_area, text="Escola Técnica Estadual Jurandir Bezerra Lins").grid(row=5,column=10,columnspan=2,padx=100)







class admin_log():
    def refresh(self):
        self.Name_entry.delete(0, "end")
        self.cpf_entry.delete(0, "end")
        self.course_entry.delete(0, "end")
        self.module_entry.delete(0, "end")
        self.senha_entry.delete(0, "end")

    def new(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()
        for row in rows:
            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()

            self.tree.insert("", tkinter.END, values=row)
            cursor.execute("""UPDATE cad1 SET nome = ?, curso =?, telefone =? cpf =?""",
                           (self.Name_entry.get(), self.course_entry.get(), self.module_entry.get(), self.cpf.get()))
            auto.commit()

        auto.commit()
        auto.close()

    def view_user(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM aluno")
        rows = cur.fetchall()
        for row in rows:

            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()

            self.tree.insert("", tkinter.END, values=row)
            self.a = self.cpf_entry.get()
            cursor.execute("""UPDATE aluno SET password =? WHERE username =?""",
                           (self.senha_entry.get(), self.a))
            auto.commit()


        auto.commit()
        auto.close()



    def view(self):
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()
        for row in rows:
            listmain = (row[0],row[1],row[2],row[3])
            auto = sqlite3.connect('cadastros.db')
            cursor = auto.cursor()

            self.tree.insert("", tkinter.END, values=listmain)
            self.jhin = self.cpf_entry.get()
            cursor.execute("""UPDATE cad1 SET nome = ?, curso =?, telefone =? WHERE cpf =?""",
                           (self.Name_entry.get(), self.course_entry.get(), self.module_entry.get(), self.jhin))
            auto.commit()


        auto.commit()
        auto.close()

    def cadastro(self):
        self.loop = False
        auto = sqlite3.connect("cadastros.db")
        cur = auto.cursor()
        cur.execute("SELECT * FROM cad1")
        rows = cur.fetchall()
        for row in rows:
            if self.cpf_entry.get() == row[1]:
                self.loop = True
        if self.loop == True:
            messagebox.showerror("Erro","Cpf já cadastrado!")
            pass
        elif self.Name_entry.get() == "":
                        messagebox.showerror("Erro","Digite o nome do aluno!")
                        pass
        elif self.cpf_entry.get() == "":
                        messagebox.showerror("Erro","Digite o cpf do aluno!")
                        pass
        elif self.course_entry.get() == "":
                        messagebox.showerror("Erro","Digite o curso do aluno!")
                        pass

        else:

                        auto = sqlite3.connect('cadastros.db')
                        cursor = auto.cursor()

                        cursor.execute("""INSERT INTO cad1 (nome, cpf, curso, telefone)
                                           VALUES (?,?,?,?)""",(self.Name_entry.get(), self.cpf_entry.get(), self.course_entry.get(), self.module_entry.get()))
                        cursor.execute("""INSERT INTO aluno (username,password)
                                           VALUES (?,?)""",(self.cpf_entry.get(), self.senha_entry.get()))
                        auto.commit()
                        self.refresh()
                        for i in self.tree.get_children():
                            self.tree.delete(i)
                        self.view()

                        messagebox.showinfo("Alerta Banco de Dados", "Cadastro realizado com sucesso")


                        auto.close()


    def att(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.jhin = self.cpf_entry.get()
        cursor.execute("""UPDATE cad1 SET nome = ?, curso =?, telefone =? WHERE cpf =?""",
                       (self.Name_entry.get(), self.course_entry.get(), self.module_entry.get(), self.jhin))
        auto.commit()
        self.refresh()
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.view()
        messagebox.showinfo("Alerta Banco de Dados", "Atualização realizada com sucesso")

        auto.close()



    def delete(self):
        auto = sqlite3.connect('cadastros.db')
        cursor = auto.cursor()
        self.rakan = self.cpf_entry.get()
        if self.rakan == "":
            messagebox.showerror("Erro","Campos vazios")
        else:
            cursor.execute(""" DELETE FROM cad1 WHERE cpf =? """, (self.rakan,))
            auto.commit()
            self.refresh()

            for i in self.tree.get_children():
                self.tree.delete(i)
            self.view()


            messagebox.showinfo("Alerta Banco de Dados", "Exclusão realizada com sucesso")
            auto.close()


    def bindp(self,event):
        self.refresh()



        for n in self.tree.selection():
            column1,column2,column3,column4, = self.tree.item(n,'values')
            if column1 == 0:
                    pass
            else:
                self.Name_entry.insert(END, column1)
                self.cpf_entry.insert(END, column2)
                self.course_entry.insert(END, column3)
                self.module_entry.insert(END, column4)








    def __init__(self):
        self.admin_window = Tk()
        self.admin_window.resizable(False, False)
        self.admin_window.iconbitmap("logo.ico")
        self.admin_window.title("Cadastro de Alunos - Módulo 1")

        # Labels----------------------------------------------------------------

        self.Name_Label = Label(self.admin_window, text="Nome", font="Times")
        self.Name_Label.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.cpf_Label = Label(self.admin_window, text="CPF", font="Times")
        self.cpf_Label.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        self.course_Label = Label(self.admin_window, text="Curso", font="Times")
        self.course_Label.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.module_Label = Label(self.admin_window, text="Telefone", font="Times")
        self.module_Label.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.senha_Label = Label(self.admin_window, text="Senha",font="Times")
        self.senha_Label.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        # Entrys-------------------------------------------------------------------

        self.Name_entry = ttk.Entry(self.admin_window, font="Times", foreground='black')
        self.Name_entry.grid(row=0, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.cpf_entry = ttk.Entry(self.admin_window, font="Times", foreground='black')
        self.cpf_entry.grid(row=1, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.course_entry = ttk.Entry(self.admin_window, font="Times", foreground='black')
        self.course_entry.grid(row=2, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.module_entry = ttk.Entry(self.admin_window, font="Times", foreground='black')
        self.module_entry.grid(row=3, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        self.senha_entry = ttk.Entry(self.admin_window, font="Times", foreground='black')
        self.senha_entry.grid(row=4, column=1, columnspan=2, sticky=W + E, padx=10, pady=0)

        # Buttons-----------------------------------------------------------------------------

        self.submit_button = ttk.Button(self.admin_window, text="Cadastrar", command=self.cadastro)
        self.submit_button.grid(row=0, column=3, padx=9, sticky=W + E)

        self.update_button = ttk.Button(self.admin_window, text="Atualizar", command=self.att)
        self.update_button.grid(row=1, column=3, padx=9, sticky=W + E)

        self.delete_button = ttk.Button(self.admin_window, text="Deletar", command=self.delete)
        self.delete_button.grid(row=2, column=3, padx=9, sticky=W + E)

        # Registers----------------------------------------------------------------------


        self.tree = ttk.Treeview(self.admin_window, selectmode="browse",
                                 column=("column1", "column2", "column3", "column4"),
                                 show='headings')
        self.tree.column("column1", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#1", text="Nome")

        self.tree.column("column2", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#2", text="CPF")

        self.tree.column("column3", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#3", text="Curso")

        self.tree.column("column4", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#4", text="Telefone")

        self.tree.grid(row=5, column=0, columnspan=6, padx=9, sticky=W + E)

        self.vsb = ttk.Scrollbar(self.admin_window, orient="vertical", command=self.tree.yview)
        self.vsb.place(x=30+360+2, y=170, height=200+20)

        self.tree.configure(yscrollcommand=self.vsb.set)

        self.tree.bind('<Double-1>',self.bindp)


        # Search---------------------------------------------------------------------------



        Label(self.admin_window, text="ETE - Jurandir Bezerra Lins").grid(row=6, column=1, columnspan=2, sticky=E,
                                                                          padx=9, pady=9)



        self.view()




        self.admin_window.mainloop()


class signinwindow():

    def view_user(self):
        self.x = Tk()
        self.x.resizable(False, False)
        self.x.iconbitmap("logo.ico")
        self.x.title("Lista de Usuários")

        # Registers----------------------------------------------------------------------

        self.tree = ttk.Treeview(self.x, selectmode="browse", column=("column1", "column2"), show='headings')
        self.tree.heading("#1", text="Nome")
        self.tree.heading("#2", text="CPF")

        self.tree.tag_configure('1', background='yellow')
        self.tree.tag_configure('1', background='blue')

        self.tree.grid(row=0, column=0, columnspan=4, padx=9, sticky=W + E)

        Button(self.x, text="Limpar Usuários").grid(row=1, column=0, columnspan=4, padx=9, sticky=W + E)

        self.x.mainloop()

    def __init__(self):
        self.signin_window = Tk()
        self.signin_window.resizable(False, False)
        self.signin_window.iconbitmap("logo.ico")
        self.signin_window.title("Cadastro")

        Label(self.signin_window, text="Cadastrar", font="Times").grid(row=0, column=0, sticky=W, pady=10)
        Label(self.signin_window, text="Usuário: ", font="Times,12", foreground='black').grid(row=1, column=0, sticky=W,
                                                                                              pady=10)
        Label(self.signin_window, text="Senha: ", font="Times", foreground='black').grid(row=2, column=0, sticky=W,
                                                                                         pady=(0, 20))

        Entry(self.signin_window, font="Times", foreground='black').grid(row=1, column=1, sticky=W, pady=10)
        Entry(self.signin_window, font="Times").grid(row=2, column=1, sticky=W, pady=(0, 20))

        user_add = Button(self.signin_window, text="Cadastrar", font="Times", background='white')
        user_add.grid(row=5, column=3, padx=20)
        view = Button(self.signin_window, text="Visualizar Cadastros", font="Times", background='white',
                      command=self.view_user)
        view.grid(row=4, column=1, rowspan=2, columnspan=4, padx=20, pady=(0, 20), sticky=W + E)

        self.signin_window.mainloop()


class loginwindow():



    def close(self):

        self.root.destroy()

    def logar(self):
        self.codex = str(self.var.get())
        if self.codex == "2":
            try:
                with sqlite3.connect('professor.db') as db:
                    c = db.cursor()
                find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
                c.execute(find_user, [(self.username.get()), (self.password.get())])
                result = c.fetchall()
                if result:
                    try:

                        self.login_window.destroy()

                        choice()







                    except:
                        print("erro prof")
                else:
                    messagebox.showerror("Acesso Negado", "Usuário Inválido")
            except:
                print("erro 12")
        elif self.codex == "1":
            try:
                with sqlite3.connect('cadastros.db') as db:
                    c = db.cursor()
                find_user = ('SELECT * FROM aluno WHERE username = ? and password = ?')
                c.execute(find_user, [(self.username.get()), (self.password.get())])
                result = c.fetchall()
                if result:
                    try:
                        global validate_user

                        validate_user=(self.username.get())

                        self.login_window.destroy()
                        area_use()


                    except:
                        pass
                else:
                    messagebox.showerror("Acesso Negado", "Usuário Inválido")
            except:
                print("erro 12")



    def logger(self):
        admin_log()

    def __init__(self):

        self.login_window = Toplevel()
        self.login_window.resizable(False, False)
        self.login_window.iconbitmap("logo.ico")

        Label(self.login_window, text="Login", font="Times").grid(row=0, column=0, sticky=W, pady=10)
        Label(self.login_window, text="Usuário: ", font="Times,12", foreground='black').grid(row=1, column=0, sticky=W,
                                                                                             pady=10)
        Label(self.login_window, text="Senha: ", font="Times", foreground='black').grid(row=2, column=0, sticky=W,
                                                                                        pady=10)

        self.username = Entry(self.login_window, font="Times", foreground='black')
        self.username.grid(row=1, column=1, sticky=W, pady=10)
        self.password = Entry(self.login_window, font="Times", show="*")
        self.password.grid(row=2, column=1, sticky=W, pady=10)

        self.but = Button(self.login_window, text="Entrar", font="Times", command=self.logar)
        self.but.grid(row=4, column=1, rowspan=2, pady=30)
        self.var = IntVar()

        self.log_u = Radiobutton(self.login_window, text="Usuário", variable=self.var, value=1).grid(row=3, column=0,
                                                                                                     pady=15, padx=30)
        self.log_a = Radiobutton(self.login_window, text="Professor", variable=self.var, value=2).grid(row=3, column=1)

        self.login_window.mainloop()


class main:

    def about_us(self):
        messagebox.showinfo("Sobre",
                            """Este sistema foi com o intuito de gerenciar de forma simples e prática as informações acadêmicas dos alunos e é totalmente open source baseado na licença MIT """)


    def create_signinwindow(self):
        try:

            signinwindow()
        except:
            raise Exception("critic from")

    def browser(self):
        import os, webbrowser
        from urllib.request import pathname2url
        url = 'file:{}'.format(pathname2url(os.path.abspath('https://github.com/Fukojima/Seete')))
        webbrowser.open(url)

    def create_login(self):
        try:
            loginwindow()



        except:
            raise Exception("critic from")

    def close(self):

        self.root.destroy()

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False,False)

        self.root.iconbitmap("logo.ico")
        self.root.title("SEETE")
        self.img = ImageTk.PhotoImage(Image.open("logo1.png"))
        self.panel = Label(self.root, image=self.img)
        self.panel.grid(row=0, column=0)

        Label(self.root, text="SEETE", font="Times,20", foreground='red4').grid(row=1, column=0, sticky=W + E, padx=40)
        Label(self.root, text="SISTEMA PARA GESTÃO ESCOLAR", font="Times,20", foreground='red4').grid(row=2,
                                                                                                             column=0,
                                                                                                             sticky=W + E,
                                                                                                             padx=40)

        self.but = Button(self.root, text="Login", command=self.create_login)
        self.but.configure(width=18, height=2, foreground='white', background="green4")
        self.but.grid(row=5, column=0, columnspan=2, sticky=N, pady=30)

        self.menu = Menu(self.root)
        self.menu.add_separator()


        self.menu.add_separator()

        self.help = Menu(self.menu, tearoff=0)
        self.help.add_command(label="Github", command=self.browser)
        self.help.add_separator()
        self.help.add_command(label="Sobre", command=self.about_us)
        self.menu.add_cascade(label="Info", menu=self.help)


        self.root.configure(menu=self.menu)
        self.root.mainloop()



try:
    main()


except:
    raise Exception("Erro critico")


