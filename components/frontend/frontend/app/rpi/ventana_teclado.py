#Author: Oscar Valverde Escobar

import tkinter as tk
from tkinter import ttk

class VentanaTeclado(tk.Toplevel):
# class VentanaTeclado(tk.Tk):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        # self = tk.Tk()
        self.callback = callback

        self.title('Teclado')

        self.config(width=800, height=440)
        # self.geometry('800x440')  # Window size
        # self.maxsize(width=800, height=440)
        # self.minsize(width=800, height=440)

        self.style = ttk.Style()
        self.style.configure('teclado.TButton', font=('Arial', 15))
        self.style.configure('teclado.TButton', background='azure')
        self.style.configure('teclado.TButton', foreground='black')
        self.theme = "light"


        # entry box
        self.equation = tk.StringVar()
        self.Dis_entry = ttk.Entry(self, state='readonly', textvariable=self.equation, font=('Arial', 20))
        self.Dis_entry.grid(rowspan=1, columnspan=20, ipadx=200, ipady=60)


        # showing all data in display
        self.exp = ""
        self.is_shift = False
        self.theme = "light"

        self.Display()
        self.focus()
        self.grab_set()

    # Necessary functions

    def Press(self,num):
        self.exp = self.exp + str(num)
        self.equation.set(self.exp)


    def Backspace(self):
        self.exp = self.exp[:-1]
        self.equation.set(self.exp)


    def Shift(self):
        self.is_shift = not self.is_shift
        self.Display()


    def Clear(self):
        self.exp = ""
        self.equation.set(self.exp)


    def Theme(self):
        if self.theme == "dark":
            self.configure(bg='gray27')
            self.style.configure('TButton', background='gray21')
            self.style.configure('TButton', foreground='white')
            # self.style.configure('TButton', width=0)
            self.theme = "light"
        elif self.theme == "light":
            self.configure(bg='gray99')
            self.style.configure('TButton', background='azure')
            self.style.configure('TButton', foreground='black')
            # self.style.configure('TButton', width=0)
            self.theme = "dark"
        self.Display()

    def Acept(self):
        # Obtener el dato ingresado y llamar a la función
        # especificada al crear esta ventana.
        self.callback(self.Dis_entry.get())
        # Cerrar la ventana.
        self.destroy()


    def Display(self):
        if (self.is_shift):
            # Adding selfs line wise
            # First Line Button
            tilda = ttk.Button(self, text='~', width=4, command=lambda: self.Press
            ('~'), style=('teclado.TButton'))
            tilda.grid(row=1, column=0, ipadx=1, ipady=10)

            num1 = ttk.Button(self, text='!', width=4, command=lambda: self.Press
            ('!'), style=('teclado.TButton'))
            num1.grid(row=1, column=1, ipadx=1, ipady=10)

            num2 = ttk.Button(self, text='@', width=4, command=lambda: self.Press
            ('@'), style=('teclado.TButton'))
            num2.grid(row=1, column=2, ipadx=1, ipady=10)

            num3 = ttk.Button(self, text='#', width=4, command=lambda: self.Press
            ('#'), style=('teclado.TButton'))
            num3.grid(row=1, column=3, ipadx=1, ipady=10)

            num4 = ttk.Button(self, text='$', width=4, command=lambda: self.Press
            ('$'), style=('teclado.TButton'))
            num4.grid(row=1, column=4, ipadx=1, ipady=10)

            num5 = ttk.Button(self, text='%', width=4, command=lambda: self.Press
            ('%'), style=('teclado.TButton'))
            num5.grid(row=1, column=5, ipadx=1, ipady=10)

            num6 = ttk.Button(self, text='^', width=4, command=lambda: self.Press
            ('^'), style=('teclado.TButton'))
            num6.grid(row=1, column=6, ipadx=1, ipady=10)

            num7 = ttk.Button(self, text='&', width=4, command=lambda: self.Press
            ('&'), style=('teclado.TButton'))
            num7.grid(row=1, column=7, ipadx=1, ipady=10)

            num8 = ttk.Button(self, text='*', width=4, command=lambda: self.Press
            ('*'), style=('teclado.TButton'))
            num8.grid(row=1, column=8, ipadx=1, ipady=10)

            num9 = ttk.Button(self, text='(', width=4, command=lambda: self.Press
            ('('), style=('teclado.TButton'))
            num9.grid(row=1, column=9, ipadx=1, ipady=10)

            num0 = ttk.Button(self, text=')', width=4, command=lambda: self.Press
            (')'), style=('teclado.TButton'))
            num0.grid(row=1, column=10, ipadx=1, ipady=10)

            plus = ttk.Button(self, text='+', width=4, command=lambda: self.Press
            ('+'), style=('teclado.TButton'))
            plus.grid(row=1, column=11, ipadx=1, ipady=10)

            self.backspace = ttk.Button(
                self, text='<---', width=4, command=self.Backspace, style=('teclado.TButton'))
            self.backspace.grid(row=1, column=12, columnspan=2, ipadx=30, ipady=10)

            # Second Line Buttons

            tab_button = ttk.Button(self, text='Tab', width=4,
                                    command=lambda: self.Press
                                    ('\t'), style=('teclado.TButton'))
            tab_button.grid(row=2, column=0, columnspan=2, ipadx=30, ipady=10)

            Q = ttk.Button(self, text='Q', width=4, command=lambda: self.Press
            ('Q'), style=('teclado.TButton'))
            Q.grid(row=2, column=2, ipadx=1, ipady=10)

            W = ttk.Button(self, text='W', width=4, command=lambda: self.Press
            ('W'), style=('teclado.TButton'))
            W.grid(row=2, column=3, ipadx=1, ipady=10)

            E = ttk.Button(self, text='E', width=4, command=lambda: self.Press
            ('E'), style=('teclado.TButton'))
            E.grid(row=2, column=4, ipadx=1, ipady=10)

            R = ttk.Button(self, text='R', width=4, command=lambda: self.Press
            ('R'), style=('teclado.TButton'))
            R.grid(row=2, column=5, ipadx=1, ipady=10)

            T = ttk.Button(self, text='T', width=4, command=lambda: self.Press
            ('T'), style=('teclado.TButton'))
            T.grid(row=2, column=6, ipadx=1, ipady=10)

            Y = ttk.Button(self, text='Y', width=4, command=lambda: self.Press
            ('Y'), style=('teclado.TButton'))
            Y.grid(row=2, column=7, ipadx=1, ipady=10)

            U = ttk.Button(self, text='U', width=4, command=lambda: self.Press
            ('U'), style=('teclado.TButton'))
            U.grid(row=2, column=8, ipadx=1, ipady=10)

            I = ttk.Button(self, text='I', width=4, command=lambda: self.Press
            ('I'), style=('teclado.TButton'))
            I.grid(row=2, column=9, ipadx=1, ipady=10)

            O = ttk.Button(self, text='O', width=4, command=lambda: self.Press
            ('O'), style=('teclado.TButton'))
            O.grid(row=2, column=10, ipadx=1, ipady=10)

            P = ttk.Button(self, text='P', width=4, command=lambda: self.Press
            ('P'), style=('teclado.TButton'))
            P.grid(row=2, column=11, ipadx=1, ipady=10)

            curly_l = ttk.Button(
                self, text='{', width=4, command=lambda: self.Press
                ('{'), style=('teclado.TButton'))
            curly_l.grid(row=2, column=12, ipadx=1, ipady=10)

            curly_r = ttk.Button(self, text='}', width=4,
                                command=lambda: self.Press
                                ('}'), style=('teclado.TButton'))
            curly_r.grid(row=2, column=13, ipadx=1, ipady=10)

            # Third Line Buttons

            pipe = ttk.Button(self, text='|', width=4, command=lambda: self.Press
            ('|'), style=('teclado.TButton'))
            pipe.grid(row=3, column=0, ipadx=1, ipady=10)

            under = ttk.Button(self, text='_', width=4, command=lambda: self.Press
            ('_'), style=('teclado.TButton'))
            under.grid(row=3, column=1, ipadx=1, ipady=10)

            A = ttk.Button(self, text='A', width=4, command=lambda: self.Press
            ('A'), style=('teclado.TButton'))
            A.grid(row=3, column=2, ipadx=1, ipady=10)

            S = ttk.Button(self, text='S', width=4, command=lambda: self.Press
            ('S'), style=('teclado.TButton'))
            S.grid(row=3, column=3, ipadx=1, ipady=10)

            D = ttk.Button(self, text='D', width=4, command=lambda: self.Press
            ('D'), style=('teclado.TButton'))
            D.grid(row=3, column=4, ipadx=1, ipady=10)

            F = ttk.Button(self, text='F', width=4, command=lambda: self.Press
            ('F'), style=('teclado.TButton'))
            F.grid(row=3, column=5, ipadx=1, ipady=10)

            G = ttk.Button(self, text='G', width=4, command=lambda: self.Press
            ('G'), style=('teclado.TButton'))
            G.grid(row=3, column=6, ipadx=1, ipady=10)

            H = ttk.Button(self, text='H', width=4, command=lambda: self.Press
            ('H'), style=('teclado.TButton'))
            H.grid(row=3, column=7, ipadx=1, ipady=10)

            J = ttk.Button(self, text='J', width=4, command=lambda: self.Press
            ('J'), style=('teclado.TButton'))
            J.grid(row=3, column=8, ipadx=1, ipady=10)

            K = ttk.Button(self, text='K', width=4, command=lambda: self.Press
            ('K'), style=('teclado.TButton'))
            K.grid(row=3, column=9, ipadx=1, ipady=10)

            L = ttk.Button(self, text='L', width=4, command=lambda: self.Press
            ('L'), style=('teclado.TButton'))
            L.grid(row=3, column=10, ipadx=1, ipady=10)

            Ñ = ttk.Button(self, text='Ñ', width=4, command=lambda: self.Press
            ('Ñ'), style=('teclado.TButton'))
            Ñ.grid(row=3, column=11, ipadx=1, ipady=10)

            colon = ttk.Button(self, text=':', width=4,
                            command=lambda: self.Press
                            (':'), style=('teclado.TButton'))
            colon.grid(row=3, column=12, ipadx=1, ipady=10)

            quotation = ttk.Button(self, text='"', width=4,
                                command=lambda: self.Press
                                ('"'), style=('teclado.TButton'))
            quotation.grid(row=3, column=13, ipadx=1, ipady=10)

            # Fourth line Buttons

            shift = ttk.Button(self, text='Shift', width=4, command=self.Shift, style=('teclado.TButton'))
            shift.grid(row=4, column=0, columnspan=2, ipadx=30, ipady=10)

            ang_l = ttk.Button(self, text='<', width=4, command=lambda: self.Press
            ('<'), style=('teclado.TButton'))
            ang_l.grid(row=4, column=2, ipadx=1, ipady=10)

            Z = ttk.Button(self, text='Z', width=4, command=lambda: self.Press
            ('Z'), style=('teclado.TButton'))
            Z.grid(row=4, column=3, ipadx=1, ipady=10)

            X = ttk.Button(self, text='X', width=4, command=lambda: self.Press
            ('X'), style=('teclado.TButton'))
            X.grid(row=4, column=4, ipadx=1, ipady=10)

            C = ttk.Button(self, text='C', width=4, command=lambda: self.Press
            ('C'), style=('teclado.TButton'))
            C.grid(row=4, column=5, ipadx=1, ipady=10)

            V = ttk.Button(self, text='V', width=4, command=lambda: self.Press
            ('V'), style=('teclado.TButton'))
            V.grid(row=4, column=6, ipadx=1, ipady=10)

            B = ttk.Button(self, text='B', width=4, command=lambda: self.Press
            ('B'), style=('teclado.TButton'))
            B.grid(row=4, column=7, ipadx=1, ipady=10)

            N = ttk.Button(self, text='N', width=4, command=lambda: self.Press
            ('N'), style=('teclado.TButton'))
            N.grid(row=4, column=8, ipadx=1, ipady=10)

            M = ttk.Button(self, text='M', width=4, command=lambda: self.Press
            ('M'), style=('teclado.TButton'))
            M.grid(row=4, column=9, ipadx=1, ipady=10)

            comma = ttk.Button(self, text=',', width=4, command=lambda: self.Press
            (','), style=('teclado.TButton'))
            comma.grid(row=4, column=10, ipadx=1, ipady=10)

            question = ttk.Button(self, text='?', width=4,
                                command=lambda: self.Press
                                ('?'), style=('teclado.TButton'))
            question.grid(row=4, column=11, ipadx=1, ipady=10)

            enter = ttk.Button(self, text='Intro', width=4,
                            command=lambda: self.Press
                            ('\n'), style=('teclado.TButton'))
            enter.grid(row=4, column=12, columnspan=2, ipadx=30, ipady=10)

            # Fifth Line Buttons

            # self.theme = ttk.Button(self, text='Theme', width=4, command=self.Theme)
            # self.theme.grid(row=5, column=0, columnspan=2, ipadx=30, ipady=10)

            space = ttk.Button(self, text='Space', width=4,
                            command=lambda: self.Press
                            (' '), style=('teclado.TButton'))
            space.grid(row=5, column=2, columnspan=8, ipadx=200, ipady=10)

            clear = ttk.Button(self, text='Limpiar', width=4, command=self.Clear, style=('teclado.TButton'))
            clear.grid(row=5, column=10, columnspan=2, ipadx=30, ipady=10)

            self.aceptar = ttk.Button(self, text='Aceptar', width=4, command=self.Acept, style=('teclado.TButton'))
            self.aceptar.grid(row=5, column=12, columnspan=2, ipadx=30, ipady=10)

            self.mainloop()
        else:
            # Adding selfs line wise
            # First Line Button
            tick = ttk.Button(self, text='`', width=4, command=lambda: self.Press
            ('`'), style=('teclado.TButton'))
            tick.grid(row=1, column=0, ipadx=1, ipady=10)

            num1 = ttk.Button(self, text='1', width=4, command=lambda: self.Press
            ('1'), style=('teclado.TButton'))
            num1.grid(row=1, column=1, ipadx=1, ipady=10)

            num2 = ttk.Button(self, text='2', width=4, command=lambda: self.Press
            ('2'), style=('teclado.TButton'))
            num2.grid(row=1, column=2, ipadx=1, ipady=10)

            num3 = ttk.Button(self, text='3', width=4, command=lambda: self.Press
            ('3'), style=('teclado.TButton'))
            num3.grid(row=1, column=3, ipadx=1, ipady=10)

            num4 = ttk.Button(self, text='4', width=4, command=lambda: self.Press
            ('4'), style=('teclado.TButton'))
            num4.grid(row=1, column=4, ipadx=1, ipady=10)

            num5 = ttk.Button(self, text='5', width=4, command=lambda: self.Press
            ('5'), style=('teclado.TButton'))
            num5.grid(row=1, column=5, ipadx=1, ipady=10)

            num6 = ttk.Button(self, text='6', width=4, command=lambda: self.Press
            ('6'), style=('teclado.TButton'))
            num6.grid(row=1, column=6, ipadx=1, ipady=10)

            num7 = ttk.Button(self, text='7', width=4, command=lambda: self.Press
            ('7'), style=('teclado.TButton'))
            num7.grid(row=1, column=7, ipadx=1, ipady=10)

            num8 = ttk.Button(self, text='8', width=4, command=lambda: self.Press
            ('8'), style=('teclado.TButton'))
            num8.grid(row=1, column=8, ipadx=1, ipady=10)

            num9 = ttk.Button(self, text='9', width=4, command=lambda: self.Press
            ('9'), style=('teclado.TButton'))
            num9.grid(row=1, column=9, ipadx=1, ipady=10)

            num0 = ttk.Button(self, text='0', width=4, command=lambda: self.Press
            ('0'), style=('teclado.TButton'))
            num0.grid(row=1, column=10, ipadx=1, ipady=10)

            equal = ttk.Button(self, text='=', width=4, command=lambda: self.Press
            ('='), style=('teclado.TButton'))
            equal.grid(row=1, column=11, ipadx=1, ipady=10)

            self.backspace = ttk.Button(
                self, text='<---', width=4, command=self.Backspace, style=('teclado.TButton'))
            self.backspace.grid(row=1, column=12, columnspan=2, ipadx=30, ipady=10)

            # Second Line Buttons

            tab_button = ttk.Button(self, text='Tab', width=4,
                                    command=lambda: self.Press
                                    ('\t'), style=('teclado.TButton'))
            tab_button.grid(row=2, column=0, columnspan=2, ipadx=30, ipady=10)

            Q = ttk.Button(self, text='q', width=4, command=lambda: self.Press
            ('q'), style=('teclado.TButton'))
            Q.grid(row=2, column=2, ipadx=1, ipady=10)

            W = ttk.Button(self, text='w', width=4, command=lambda: self.Press
            ('w'), style=('teclado.TButton'))
            W.grid(row=2, column=3, ipadx=1, ipady=10)

            E = ttk.Button(self, text='e', width=4, command=lambda: self.Press
            ('e'), style=('teclado.TButton'))
            E.grid(row=2, column=4, ipadx=1, ipady=10)

            R = ttk.Button(self, text='r', width=4, command=lambda: self.Press
            ('r'), style=('teclado.TButton'))
            R.grid(row=2, column=5, ipadx=1, ipady=10)

            T = ttk.Button(self, text='t', width=4, command=lambda: self.Press
            ('t'), style=('teclado.TButton'))
            T.grid(row=2, column=6, ipadx=1, ipady=10)

            Y = ttk.Button(self, text='y', width=4, command=lambda: self.Press
            ('y'), style=('teclado.TButton'))
            Y.grid(row=2, column=7, ipadx=1, ipady=10)

            U = ttk.Button(self, text='u', width=4, command=lambda: self.Press
            ('u'), style=('teclado.TButton'))
            U.grid(row=2, column=8, ipadx=1, ipady=10)

            I = ttk.Button(self, text='i', width=4, command=lambda: self.Press
            ('i'), style=('teclado.TButton'))
            I.grid(row=2, column=9, ipadx=1, ipady=10)

            O = ttk.Button(self, text='o', width=4, command=lambda: self.Press
            ('o'), style=('teclado.TButton'))
            O.grid(row=2, column=10, ipadx=1, ipady=10)

            P = ttk.Button(self, text='p', width=4, command=lambda: self.Press
            ('p'), style=('teclado.TButton'))
            P.grid(row=2, column=11, ipadx=1, ipady=10)

            sq_l = ttk.Button(self, text='[', width=4, command=lambda: self.Press
            ('['), style=('teclado.TButton'))
            sq_l.grid(row=2, column=12, ipadx=1, ipady=10)

            sq_r = ttk.Button(self, text=']', width=4, command=lambda: self.Press
            (']'), style=('teclado.TButton'))
            sq_r.grid(row=2, column=13, ipadx=1, ipady=10)

            # Third Line Buttons

            back_slash = ttk.Button(self, text='\\', width=4,
                                    command=lambda: self.Press
                                    ('\\'), style=('teclado.TButton'))
            back_slash.grid(row=3, column=0, ipadx=1, ipady=10)

            minus = ttk.Button(self, text='-', width=4, command=lambda: self.Press
            ('-'), style=('teclado.TButton'))
            minus.grid(row=3, column=1, ipadx=1, ipady=10)

            A = ttk.Button(self, text='a', width=4, command=lambda: self.Press
            ('a'), style=('teclado.TButton'))
            A.grid(row=3, column=2, ipadx=1, ipady=10)

            S = ttk.Button(self, text='s', width=4, command=lambda: self.Press
            ('s'), style=('teclado.TButton'))
            S.grid(row=3, column=3, ipadx=1, ipady=10)

            D = ttk.Button(self, text='d', width=4, command=lambda: self.Press
            ('d'), style=('teclado.TButton'))
            D.grid(row=3, column=4, ipadx=1, ipady=10)

            F = ttk.Button(self, text='f', width=4, command=lambda: self.Press
            ('f'), style=('teclado.TButton'))
            F.grid(row=3, column=5, ipadx=1, ipady=10)

            G = ttk.Button(self, text='g', width=4, command=lambda: self.Press
            ('g'), style=('teclado.TButton'))
            G.grid(row=3, column=6, ipadx=1, ipady=10)

            H = ttk.Button(self, text='h', width=4, command=lambda: self.Press
            ('h'), style=('teclado.TButton'))
            H.grid(row=3, column=7, ipadx=1, ipady=10)

            J = ttk.Button(self, text='j', width=4, command=lambda: self.Press
            ('j'), style=('teclado.TButton'))
            J.grid(row=3, column=8, ipadx=1, ipady=10)

            K = ttk.Button(self, text='k', width=4, command=lambda: self.Press
            ('k'), style=('teclado.TButton'))
            K.grid(row=3, column=9, ipadx=1, ipady=10)

            L = ttk.Button(self, text='l', width=4, command=lambda: self.Press
            ('l'), style=('teclado.TButton'))
            L.grid(row=3, column=10, ipadx=1, ipady=10)

            Ñ = ttk.Button(self, text='ñ', width=4, command=lambda: self.Press
            ('ñ'), style=('teclado.TButton'))
            Ñ.grid(row=3, column=11, ipadx=1, ipady=10)

            semi_co = ttk.Button(self, text=';', width=4,
                                command=lambda: self.Press
                                (';'), style=('teclado.TButton'))
            semi_co.grid(row=3, column=12, ipadx=1, ipady=10)

            quotation = ttk.Button(self, text="'", width=4,
                                command=lambda: self.Press
                                ("'"), style=('teclado.TButton'))
            quotation.grid(row=3, column=13, ipadx=1, ipady=10)

            # Fourth line Buttons         

            shift = ttk.Button(self, text='Shift', width=4, command=self.Shift, style=('teclado.TButton'))
            shift.grid(row=4, column=0, columnspan=2, ipadx=30, ipady=10)

            ang_r = ttk.Button(self, text='>', width=4, command=lambda: self.Press
            ('>'), style=('teclado.TButton'))
            ang_r.grid(row=4, column=2, ipadx=1, ipady=10)

            Z = ttk.Button(self, text='z', width=4, command=lambda: self.Press
            ('z'), style=('teclado.TButton'))
            Z.grid(row=4, column=3, ipadx=1, ipady=10)

            X = ttk.Button(self, text='x', width=4, command=lambda: self.Press
            ('x'), style=('teclado.TButton'))
            X.grid(row=4, column=4, ipadx=1, ipady=10)

            C = ttk.Button(self, text='c', width=4, command=lambda: self.Press
            ('c'), style=('teclado.TButton'))
            C.grid(row=4, column=5, ipadx=1, ipady=10)

            V = ttk.Button(self, text='v', width=4, command=lambda: self.Press
            ('v'), style=('teclado.TButton'))
            V.grid(row=4, column=6, ipadx=1, ipady=10)

            B = ttk.Button(self, text='b', width=4, command=lambda: self.Press
            ('b'), style=('teclado.TButton'))
            B.grid(row=4, column=7, ipadx=1, ipady=10)

            N = ttk.Button(self, text='n', width=4, command=lambda: self.Press
            ('n'), style=('teclado.TButton'))
            N.grid(row=4, column=8, ipadx=1, ipady=10)

            M = ttk.Button(self, text='m', width=4, command=lambda: self.Press
            ('m'), style=('teclado.TButton'))
            M.grid(row=4, column=9, ipadx=1, ipady=10)

            dot = ttk.Button(self, text='.', width=4, command=lambda: self.Press
            ('.'), style=('teclado.TButton'))
            dot.grid(row=4, column=10, ipadx=1, ipady=10)

            slash = ttk.Button(self, text='/', width=4, command=lambda: self.Press
            ('/'), style=('teclado.TButton'))
            slash.grid(row=4, column=11, ipadx=1, ipady=10)

            enter = ttk.Button(self, text='Intro', width=4,
                            command=lambda: self.Press
                            ('\n'), style=('teclado.TButton'))
            enter.grid(row=4, column=12, columnspan=2, ipadx=30, ipady=10)

            # Fifth Line Buttons

            # self.theme = ttk.Button(self, text='Theme', width=4, command=self.Theme)
            # self.theme.grid(row=5, column=0, columnspan=2, ipadx=30, ipady=10)

            space = ttk.Button(self, text='Space', width=4,
                            command=lambda: self.Press
                            (' '), style=('teclado.TButton'))
            space.grid(row=5, column=2, columnspan=8, ipadx=200, ipady=10)

            clear = ttk.Button(self, text='Limpiar', width=4, command=self.Clear, style=('teclado.TButton'))
            clear.grid(row=5, column=10, columnspan=2, ipadx=30, ipady=10)

            self.aceptar = ttk.Button(self, text='Aceptar', width=4, command=self.Acept, style=('teclado.TButton'))
            self.aceptar.grid(row=5, column=12, columnspan=2, ipadx=30, ipady=10)


# ventana_teclado = VentanaTeclado()
# ventana_teclado.mainloop()            

