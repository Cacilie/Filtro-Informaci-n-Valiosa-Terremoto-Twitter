class Tuit:

    def __init__(self, user, text):
        self.user = user
        self.text = text

    def toString(self):
        return str("Usuario: " + self.user + " Text: " + self.text)


        
