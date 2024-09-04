class Triangulo:
    def __init__(self, ladoA,ladoB,ladoC):
        self.ladoA=ladoA
        self.ladoB=ladoB
        self.ladoC=ladoC
    def perg(self):
        a=int(input("Digite o valor do lado A: "))
        b=int(input("Digite o valor do lado B: "))
        c=int(input("Digite o valor do lado C: "))
        
        calculo = a+b+c
        print(f"Perimetro: {calculo}")

        if a>b and a>c:
            print(f"Maior lado é: {a}")

        if b>a and b>c:
            print(f"Maior lado é: {b}")

        if c>a and c>b :
            print(f"Maior lado é: {c}")


triang1=Triangulo(0,0,0)
triang1.perg()