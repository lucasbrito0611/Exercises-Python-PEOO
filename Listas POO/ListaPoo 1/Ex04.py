class Cinema:
    def __init__(self):
        self.dia = input('Digite o dia da semana: ')
        self.horario = input('Digite o horário: ').split(':')

    def valor(self):
        ingresso = ''
        hora = int(self.horario[0])
        minutos = int(self.horario[1])

        if self.dia == 'Quarta':
            ingresso = 8
            
            return (f'Inteira = R$ {ingresso:.2f}\nMeia = R$ {ingresso:.2f}')
            
        if self.dia != 'Quarta':
            if self.dia == 'Segunda' or self.dia == 'Terça' or self.dia == 'Quinta':
                ingresso = 16
            elif self.dia == 'Sexta' or self.dia == 'Sábado' or self.dia == 'Domingo':
                ingresso = 20
    
            if 17 <= hora <= 23 or hora == 0 and minutos == 0:
                ingresso += (ingresso * 0.5)

        
            return (f'Inteira = R$ {ingresso:.2f}\nMeia = R$ {ingresso/2:.2f}')
        

x = Cinema()

print(x.valor())