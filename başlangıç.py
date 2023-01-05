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

def main():
    run = True




    def çizmek():
        EKRAN.blit(BG, (0,0))

        py.display.update()


    while run:
        çizmek()

        for event in py.event.get():
            if event.type == py.QUIT:
                run =False

main()