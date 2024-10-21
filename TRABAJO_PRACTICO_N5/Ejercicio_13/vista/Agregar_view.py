from customtkinter import *

class Agregar_view:
    
    def __init__(self):
        self.__ventana = CTk()
        self.__ventana.title('Abm Clima')
        posx = 400
        posy = 200
        self.__ventana.geometry("800x640+{}+{}".format(posx,posy))
        
        self.__lbl_tipo_clima = CTkLabel(self.__ventana, text="Tipo Clima",width=100, height=30)
        self.__lbl_tipo_clima.place(relx=0.2,rely=0.10)
        self.__txt_tipo_clima = CTkEntry(self.__ventana, width=100, height=20)
        self.__txt_tipo_clima.place(relx=0.35,rely=0.11)
        
        self.__lbl_fecha = CTkLabel(self.__ventana, text="Fecha",width=100, height=30)
        self.__lbl_fecha.place(relx=0.2,rely=0.15)
        self.__txt_fecha = CTkEntry(self.__ventana, width=100, height=20)
        self.__txt_fecha.place(relx=0.35,rely=0.16)
        
        self.__lbl_hora = CTkLabel(self.__ventana, text="Hora",width=100, height=30)
        self.__lbl_hora.place(relx=0.2,rely=0.20)
        self.__txt_hora = CTkEntry(self.__ventana, width=100, height=20)
        self.__txt_hora.place(relx=0.35,rely=0.21)
        
        self.__btn_agregar = CTkButton(self.__ventana, text='Agregar', width=100, height=20)
        self.__btn_agregar.place(relx=0.35,rely=0.32)
    
    def get_ventana(self):
        return self.__ventana
    
    def get_btn_agregar(self):
        return self.__btn_agregar
    
    def get_txt_tipo_clima(self):
        return self.__txt_tipo_clima
    
    def get_txt_fecha(self):
        return self.__txt_fecha
    
    def get_txt_hora(self):
        return self.__txt_hora
    
