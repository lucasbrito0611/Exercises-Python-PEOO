# class Musica:
#     def __init__(self, titulo, artista, album):
#         self.__titulo = titulo
#         self.__artista = artista
#         self.__album = album
#         # self.__datainclusao = datainclusao
#         # self.__duracao = duracao

#     def __str__(self):
#         return f'Titulo: {self.__titulo} - Artista: {self.__artista} - Álbum: {self.__album}'
    
# class Playlist():
#     def __init__(self, nome, descricao):
#         self.__nome = nome
#         self.__descricao = descricao
#         self.__musicas = []

#     def Inserir(self, musica):
#         if musica in self.__musicas:
#             return 'Erro'
        
#         self.__musicas.append(musica)
#         return musica
    
#     def Listar(self):
#         return self.__musicas
    
#     def __str__(self):
#         return f'Nome: {self.__nome} - Descrição: {self.__descricao} '
    
# class UI:
#     @staticmethod
#     def menu():
#         print('1 - Nova playlist, 2 - Inserir musica, 3 - Listar playlist, 0 - Fim: ')
        
#     def main():
#         op = None
#         play = None
        
#         while op != 0:
#             if op == 1:
#                 nome = input('Nome da playlist: ')
#                 descricao = input('Descrição da playlist: ')
#                 play = Playlist(nome, descricao)
#                 print(play)
#             if op == 2:    
#                 if play == None:
#                     print('Crie uma playlist antes de inserir músicas.')
#                 else:
#                     titulo = input('Título da música: ')
#                     artista = input('Artista da música: ')
#                     album = input('Álbum da música: ')
#                     music = Musica(titulo, artista, album)
#                     inserir = play.Inserir(music)
#                     if inserir == 'Erro':
#                         print('Essa música já foi inserida.')
#                     else:
#                         print('Música inserida:', inserir)
#             if op == 3:
#                 if play == None:
#                     print('Crie uma playlist antes de listar as músicas.')
#                 else:
#                     print('Músicas na playlist:', play.Listar())
            
#             op = int(input('1 - Nova playlist, 2 - Inserir musica, 3 - Listar playlist, 0 - Fim: '))

# UI.main()

# ------------------------------------------------------------------

import datetime

class Musica:
    def __init__(self, titulo, artista, album, duracao):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        # self.__datainclusao = datetime.datetime.today()
        self.__duracao = duracao

    def __str__(self):
        # data = self.__datainclusao.strftime("%d/%m/%Y")
        return f'{self.__titulo} - {self.__artista} - {self.__album} - {self.__duracao}'

    def get_duracao(self):
        return self.__duracao
    
class Playlist():
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []

    def Inserir(self, musica):
        if musica in self.__musicas:
            return 'Erro'
        else:
            self.__musicas.append(musica)

    def tempo_total(self):
        total = datetime.timedelta()
        for i in self.__musicas:
            total += i.get_duracao()
        return total
        
    def Listar(self):
        return self.__musicas
    
    def __str__(self):
        return f'Nome: {self.__nome} - Descrição: {self.__descricao} '
    
class UI:
    @staticmethod
    def menu():
        print('1 - Nova playlist, 2 - Inserir musica, 3 - Listar playlist, 4 - Duração da Playlist, 0 - Fim: ')
        
    def main():
        op = None
        play = None
        
        while op != 0:
            if op == 1:
                nome = input('Nome da playlist: ')
                descricao = input('Descrição da playlist: ')
                play = Playlist(nome, descricao)
                print(play)
            if op == 2:    
                if play == None:
                    print('Crie uma playlist antes de inserir músicas.')
                else:
                    titulo = input('Título da música: ')
                    artista = input('Artista da música: ')
                    album = input('Álbum da música: ')
                    duracao_txt = input('Duração (mm:ss): ')
                    min, sec = map(int, duracao_txt.split(':'))
                    duracao = datetime.timedelta(minutes=min, seconds=sec)
                    music = Musica(titulo, artista, album, duracao)

                    play.Inserir(music)
            if op == 3:
                if play == None:
                    print('Crie uma playlist antes de listar as músicas.')
                else:
                    listar = play.Listar()
                    print('Músicas na playlist:', *listar)

            if op == 4:
                if play == None:
                    print('Crie uma playlist antes de ver a duração total.')
                else:
                    print(f'Tempo Total = {play.tempo_total()}')
            
            op = int(input('1 - Nova playlist, 2 - Inserir musica, 3 - Listar playlist, 4 - Duração da Playlist, 0 - Fim: '))

UI.main()