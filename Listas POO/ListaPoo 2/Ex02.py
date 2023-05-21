class Disciplina:
    def __init__(self):
        self.__nome = ''
        self.__nota1 = 0
        self.__nota2 = 0
        self.__nota3 = 0
        self.__nota4 = 0
        self.__notafinal = 0
    
    def set_nome(self, nome):
        if nome.isalpha(): self.__nome = nome
        else: raise ValueError()
    def set_nota1(self, nota1):
        if nota1 >= 0: self.__nota1 = nota1
        else: raise ValueError()
    def set_nota2(self, nota2):
        if nota2 >= 0: self.__nota2 = nota2
        else: raise ValueError()
    def set_nota3(self, nota3):
        if nota3 >= 0: self.__nota3 = nota3
        else: raise ValueError()
    def set_nota4(self, nota4):
        if nota4 >= 0: self.__nota4 = nota4
        else: raise ValueError()
    def set_notafinal(self, notafinal):
        if notafinal >= 0: self.__notafinal = notafinal
        else: raise ValueError()

    def get_nome(self):
        return self.__nome
    def get_nota1(self):
        return self.__nota1
    def get_nota2(self):
        return self.__nota2
    def get_nota3(self):
        return self.__nota3
    def get_nota4(self):
        return self.__nota4
    def get_notafinal(self):
        return self.__notafinal

    def calc_media_parcial(self):
        return ((self.__nota1 * 2) + (self.__nota2 * 2) +(self.__nota3 * 3) + (self.__nota4 * 3)) / 10
    def calc_media_final(self):
        return ((((self.__nota1 * 2) + (self.__nota2 * 2) +(self.__nota3 * 3) + (self.__nota4 * 3)) / 10) + (self.__notafinal)) / 2


class UI:
    @staticmethod
    def main():
        x = Disciplina()

        print('Digite o nome da disciplina:')
        nome = input()
        print('Digite a nota do primeiro bimestre:')
        nota1 = int(input())
        print('Digite a nota do segundo bimestre:')
        nota2 = int(input())
        print('Digite a nota do terceiro bimestre:')
        nota3 = int(input())
        print('Digite a nota do quarto bimestre:')
        nota4 = int(input())
        
        x.set_nome(nome)
        x.set_nota1(nota1)
        x.set_nota2(nota2)
        x.set_nota3(nota3)
        x.set_nota4(nota4)
        
        print(f'Media parcial:{x.calc_media_parcial():.0f}')
        
        if x.calc_media_parcial() >= 60:
            print('Aprovado')
        else:
            print('Digite a nota da prova final:')
            notafinal = int(input())
            
            x.set_notafinal(notafinal)
            print(f'Media final: {x.calc_media_final():.0f}')

            if x.calc_media_final() >= 60:
                print('Aprovado')
            else:
                print('Reprovado')
        
UI.main()