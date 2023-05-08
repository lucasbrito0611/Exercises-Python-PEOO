class Disciplina:
    def __init__(self):
        self.nome = ''
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.nota4 = 0
        self.notafinal = 0

    def calculo(self):
        media = ((self.nota1 * 2) +  (self.nota1 * 2) + (self.nota1 * 3) + (self.nota1 * 3)) / 10
        
        if media >= 60:
            return (f'Aprovado Direto\nMedia = {media:.0f}')
        else:
            mediafinal = ((self.notafinal + media) / 2)
            if mediafinal >= 60:
                return (f'Aprovado na Prova Final\nMedia = {mediafinal:.0f}')
            else:
                return (f'Reprovado na Prova Final\nMedia = {mediafinal:.0f}')

x = Disciplina()
x.nome = input()
x.nota1 = int(input())
x.nota2 = int(input())
x.nota3 = int(input())
x.nota4 = int(input())
x.notafinal = int(input())

print(x.calculo())