#OYUNN YAZILIMINA BAŞLANIYOR NE TARZ OYUN OLDUĞUNU SEÇ
#kullanılacak modüller eklendi

import pygame  as py
import os
import random

#penceresi yazılıyor

GENİŞLİK= 750
YÜKSEKLİK= 600
EKRAN=py.display.set_mode((GENİŞLİK,YÜKSEKLİK))

#resimleri yüklemek
#ARKAplan
BG=py.image.load(os.path.join("proje için","background_space.png"))

#Görev Gemisi
GOREV_GEMİSİ = py.image.load(os.path.join("proje için","mission_ship.png"))


class Gemi():
    def __init__(self,x,y,sağlık=100):
        self.x=x
        self.y=y
        self.sağlık=sağlık
        self.gemi_img= None
    
    def çizmek(self,ekran):
        ekran.blit(self.gemi_img,(self.x,self.y))

class OyuncuGemisi(Gemi):
    def __init__(self,x,y,sağlık=100):
        super().__init__(x,y,sağlık)
        self.gemi_img = GOREV_GEMİSİ




def main():
    run = True
    

    oyuncu = OyuncuGemisi(350,450)



    def çizmek():
        EKRAN.blit(BG, (0,0))
        oyuncu.çizmek(EKRAN)

        py.display.update()


    while run:
        çizmek()

        for event in py.event.get():
            if event.type == py.QUIT:
                run =False

        keys = py.key.get_pressed()

        if keys[py.K_LEFT]:
            oyuncu.x -= 5
        if keys[py.K_RIGHT]:
            oyuncu.x += 5
        if keys[py.K_UP]:
            oyuncu.y -=5
        if keys[py.K_DOWN]:
            oyuncu.y += 5

main()