class Cat():
    def getString(self):
        self.name = input()
    def printString(self):
        print(self.name.upper())
hola = Cat()
hola.getString()
hola.printString()