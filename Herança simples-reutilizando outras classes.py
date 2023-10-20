class Camera:
    
    def __init__(self, marca, megapixel):
        self.marca = marca
        self.megapixel = megapixel

    def tirar_foto(self):
        print('Foto tirada com a camera {}, com a qualidade de {}'
              .format(self.marca,self.megapixel))

class CameraCelular(Camera):
   
    def __init__(self, marca, megapixel, quantidade_de_cameras):
        super().__init__(marca, megapixel)
        self.quantidade_de_cameras = quantidade_de_cameras  
    
    def aplicando_filtro(self, filtro):
        print('Aplicando filtro {}'.format(filtro))
    
    def tirar_foto(self,camera_a_utilizar):
        print('Foto tirada com a camera {}, com a qualidade de {} megapixel, utilizando a câmera #{}'
             .format(self.marca,self.megapixel,camera_a_utilizar))
       
camera_celular = CameraCelular('Sony', '25mp', 4)
camera_celular.aplicando_filtro('Azul')
camera_celular.tirar_foto(2)


#super - não é mais necessário repetir as informação da classe já feita.