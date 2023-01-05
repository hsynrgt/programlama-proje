#OYUNN YAZILIMINA BAŞLANIYOR NE TARZ OYUN OLDUĞUNU SEÇ
#kullanılacak modüller eklendi

import pygame  as py
import os
import random

#penceresi yazılıyor

genişlik= 750
yükseklik= 600
ekran=py.display.set_mode((genişlik,yükseklik))

#resimleri yüklemek

BG=py.image.load(os.path.join("proje için","background_space.png"))



def main():
    run = True




    def çizmek():
        ekran.blit(BG, (0,0))

        py.display.update()


    while run:
        çizmek()

        for event in py.event.get():
            if event.type == py.QUIT:
                run =False

main()