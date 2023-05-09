class Disciplina:
    def __init__(self):
        self.nome = input('Digite o nome da disciplina: ')
        self.nota1 = int(input('Digite a nota do primeiro bimestre: '))
        self.nota2 = int(input('Digite a nota do segundo bimestre: '))
        self.nota3 = int(input('Digite a nota do terceiro bimestre: '))
        self.nota4 = int(input('Digite a nota do quarto bimestre: '))
       
    def calculo(self):
        media = ((self.nota1 * 2) +  (self.nota1 * 2) + (self.nota1 * 3) + (self.nota1 * 3)) / 10
        
        if media >= 60:
            return (f'Aprovado\nMedia = {media:.0f}')
        else:
            print('Você ficou de recuperação')
            self.notafinal = int(input('Digite a nota da prova final: '))
            mediafinal = ((self.notafinal + media) / 2)
            if mediafinal >= 60:
                return (f'Aprovado\nMedia = {mediafinal:.0f}')
            else:
                return (f'Reprovado\nMedia = {mediafinal:.0f}')

x = Disciplina()

print(x.calculo())