class Tuit:

    def __init__(self, user, text, idt):
        self.user = user
        self.text = text
        self.idt = idt

    def toString(self):
        return str("Usuario: " + self.user + " Text: " + self.text)

    def getText(self):
        return str(self.text)

    def getIdt(self):
        return self.idt


        
