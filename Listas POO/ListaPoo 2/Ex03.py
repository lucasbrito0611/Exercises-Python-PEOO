class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0
    def set_distancia(self, distancia):
        if distancia >= 0: self.__distancia = distancia         
        else: raise ValueError()
    def set_tempo(self, tempo):
        if tempo >= 0: self.__tempo = tempo  
        else: raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        if self.__tempo == 0: return 0
        return self.__distancia / self.__tempo
    
class UI:
    @staticmethod
    def main():
        v = Viagem()
       
        print('Digite a distância percorrida em km')
        distancia = float(input())
        
        print('Digite o tempo em hh:mm')
        tempo = input()
        horas, minutos = map(int, tempo.split(':'))
        horas = horas + (minutos / 60)
        
        v.set_distancia(distancia)
        v.set_tempo(horas)

        print(f'{v.velocidade_media()} km/h')

UI.main()