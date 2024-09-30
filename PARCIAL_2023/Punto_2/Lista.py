class Lista:

    def __init__(self):
        self.__lista = []

    def agregar_video(self, video):
        self.__lista.append(video)
        
    def get_lista(self):
        return self.__lista
