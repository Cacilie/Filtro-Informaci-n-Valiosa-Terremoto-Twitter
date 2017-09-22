 # -*- coding: utf-8 -*-

class Tuit:

    def __init__(self, user, text, idt):
        self.user = user.encode('utf-8')
        self.text = text.encode('utf-8')
        self.idt = idt

    def toString(self):
        return "Usuario: " + self.user + " Text: " + self.text

    def getText(self):
        #return str(self.text) // solo para caracteres ascii
        return self.text

    def getIdt(self):
        return self.idt

    def getAuthor(self):
        return self.user


        
