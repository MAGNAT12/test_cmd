a = input()

class Book:
    
    def __init__(self, a) -> None:
        self.a = a 

    def aut(self):
        print(self.a)

b = Book(a)
b.aut()