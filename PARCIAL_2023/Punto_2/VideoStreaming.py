class VideoStreaming:

    def __init__(self, titulo , descripcion , visibilidad , es_para_ninos): ## Creo el constructor de mi clase
        self.__titulo = titulo ## privado
        self._descripcion = descripcion ## privado
        self.visibilidad = visibilidad ### privado
        self.es_para_ninos = es_para_ninos ## los tributos estan en privado

    def get_titulo(self):
        return self.__titulo