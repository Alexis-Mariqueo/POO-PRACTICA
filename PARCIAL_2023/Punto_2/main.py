from VideoStreaming import VideoStreaming
from Lista import Lista

listaReproducible = Lista() ## SE CREA EL OBJETO
listaPrivada = Lista() ## SE CREA EL OBJETO 
for i in range(1,10):
    listaReproducible.agregar_video(VideoStreaming("video {}".format(i), "descripcion {}".format(i),"Publico", True)) ## se agrega contenido a la lista 
    
    listaPrivada.agregar_video(VideoStreaming("video", "descripcion", "Privado", False)) ## se agrega contenido a la lista 

for video in listaReproducible.get_lista():## Get para mostrar el contenido del objeto listaReproducible de la lista
    print(video.get_titulo()) ###Get para mostrar el contenido del objeto video del titulo