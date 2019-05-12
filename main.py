#!/usr/bin/env python3
from tkinter import *
from calc import *


class Interface(Tk):
    hauteur = 800
    largeur = 500
    memory = ""
    memory2 = ""
    operation = ""

    def __init__(self):
        Tk.__init__(self)
        self.title("Calculatrice Scientifique @Jérôme")
        self.geometry("%dx%d+560+290" % (Interface.hauteur, Interface.largeur))
        self.configure(background="white")
        self.affichage = Label(borderwidth=2, relief="sunken")
        self.affichage.configure(bg="#C0DFFF")
        self.affichage.pack()
        self.affichage.place(height=80, width=760, x=20, y=60)
        self.chaine = ""

        self.buttons = ["0", ".", "=", "+", "1", "2", "3", "-", "4", "5",
                        "6", "x", "7", "8", "9", "÷", "√", "²", "%", "AC"]
        self.caract = ["0", ".", "=", "+", "1", "2", "3", "-", "4", "5",
                       "6", "x", "7", "8", "9", "÷", "√", "²", "%", "AC"]
        self.but = []
        for i in range(0, len(self.buttons)):
            y = (Interface.hauteur / 12) * int(i/4)
            x = (Interface.largeur / 8) * int(i % 4)
            self.but.append(Button(self, bg="#CEBC96", width=4, height=3, bd=1, text=self.buttons[i],
                              command=lambda a=i: self.action(self.caract[a])))
            self.but[i].place(x=(Interface.hauteur * 2/3)+x, y=(Interface.largeur * 5/6)-y)

    def action(self, func):
        if func in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            click = str(func)
            self.chaine += click
            self.affichage['text'] = self.chaine
        else:
            if func == "+":
                Interface.operation = Calculate.add
                if Interface.memory == "":
                    Interface.memory = int(self.chaine)
                elif Interface.memory2 == "":
                    Interface.memory2 = int(self.chaine)
                self.chaine = ""
                self.affichage['text'] = ""
            if func == "-":
                Interface.operation = Calculate.subtract
                if Interface.memory == "":
                    Interface.memory = int(self.chaine)
                elif Interface.memory2 == "":
                    Interface.memory2 = int(self.chaine)
                self.chaine = ""
                self.affichage['text'] = ""

            if func == "x":
                Interface.operation = Calculate.multiply
                if Interface.memory == "":
                    Interface.memory = int(self.chaine)
                elif Interface.memory2 == "":
                    Interface.memory2 = int(self.chaine)
                self.chaine = ""
                self.affichage['text'] = ""

            if func == "÷":
                Interface.operation = Calculate.divide
                if Interface.memory == "":
                    Interface.memory = int(self.chaine)
                elif Interface.memory2 == "":
                    Interface.memory2 = int(self.chaine)
                self.chaine = ""
                self.affichage['text'] = ""

            if func == "√":
                Interface.memory = int(self.chaine)
                self.affichage['text'] = Calculate.square(Interface.memory)
                self.chaine = self.affichage['text']

            if func == "²":
                Interface.memory = int(self.chaine)
                self.affichage['text'] = Calculate.pow(Interface.memory, 2)
                self.chaine = self.affichage['text']

            if func == "=":
                Interface.memory2 = int(self.chaine)
                if Interface.memory != "" and Interface.memory2 != "":
                    self.affichage['text'] = Interface.operation(Interface.memory, Interface.memory2)
                    self.chaine = ""
                    Interface.memory = ""
                    Interface.memory2 = ""

            if func == "AC":
                self.affichage['text'] = ""
                self.chaine = ""
                Interface.memory = ""
                Interface.memory2 = ""









"""
Création de la fénêtre de la calculatrice
"""
if __name__ == "__main__":
    gui = Interface()

    gui.mainloop()
