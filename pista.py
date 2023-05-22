from turtle import Turtle

class Pista(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(4) # tamanho da caneta

        
        self.desenhar_borda(-150) #esqueda
        self.desenhar_borda(150) #direita
               
        self.desenhar_traco((30, -400))
        self.desenhar_traco((-30, -400))
        
        self.desenhar_traco((90, -400))
        self.desenhar_traco((-90, -400))

    def desenhar_borda(self, pos):
        self.penup()
        self.goto(pos, -400) # início da linha
        self.pendown()
        self.goto(pos, 400) # final da linha
        
    def desenhar_traco(self, pos):
        self.setheading(90)
        self.penup()
        self.goto(pos)
        for traco in range(30):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
            
    