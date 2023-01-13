#OYUNN YAZILIMINA BAŞLANIYOR NE TARZ OYUN OLDUĞUNU SEÇ
#kullanılacak modüller eklendi

from msilib.schema import SelfReg
from typing import Self
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

#Düşman Gemileri
KIRMIZI_DÜŞMAN_GEMİSİ = py.image.load(os.path.join("proje için", "enemy_ship_red.png"))
YEŞİL_DÜŞMAN_GEMİSİ = py.image.load(os.path.join("proje için", "enemy_ship_green.png"))
MAVİ_DÜŞMAN_GEMİSİ = py.image.load(os.path.join("proje için", "enemy_ship_blue.png"))

#Lazerler
OYUNCU_LAZER = py.image.load(os.path.join("proje için", "blue_rocket.png"))

#Düşmanların Lazerleri
LAZER01 = py.image.load(os.path.join("proje için", "laser01.png")) 
LAZER02 = py.image.load(os.path.join("proje için", "laser02.png"))
LAZER03 = py.image.load(os.path.join("proje için", "laser03.png"))



class Gemi():
    def __init__(self,x,y,sağlık=100):
        self.x=x
        self.y=y
        self.sağlık=sağlık
        self.gemi_img= None
        self.lazer_img = None

    def çizmek(self,ekran):
        ekran.blit(self.gemi_img,(self.x,self.y))

        def get_widht(self):
            return self.ship_img.get_widht()

            def get_height(self):
                return self.ship_img.get_height()

class OyuncuGemisi(Gemi):


    def __init__(self,x,y,sağlık=100):
        super().__init__(x,y,sağlık)
        self.gemi_img = GOREV_GEMİSİ
        self.lazer_img = OYUNCU_LAZER


class DüşmanGemisi(Gemi):
    RENK_HARİTASI = {
        "red"  : [KIRMIZI_DÜŞMAN_GEMİSİ, LAZER01],
        "green"  :[YEŞİL_DÜŞMAN_GEMİSİ, LAZER02],
        "blue"  :[MAVİ_DÜŞMAN_GEMİSİ, LAZER03]
}

    def __init__(self,x,y,renk,sağlık=100):
         super().__init__(x,y,sağlık)
         self.gemi_img, self.lazer_img = self.RENK_HARİTASI[renk]

    def move(self, hızı):
        self.y += hızı



def main():
    run = True
    FPS= 75
    düşmanlar = []
    düşman_hızı = 1
    düşman_uzunluk = 0

    oyuncu_hızı = 5

    clock = py.time.Clock()


    oyuncu = OyuncuGemisi(350,450)



    def çizmek():
        EKRAN.blit(BG, (0,0))
        oyuncu.çizmek(EKRAN)
        for düşman in düşmanlar:
            düşman.çizmek(EKRAN)

        py.display.update()


    while run:
        clock.tick(FPS)
        çizmek()

        if len(düşmanlar) == 0:
            düşman_hızı += 1
            düşman_uzunluk += 5
            for i in range(düşman_uzunluk):
                düşman = DüşmanGemisi(random.randrange(1,700), random.randrange(-1500,100))
            random.choice(["red","blue","green"]) 
            düşman.append(düşman)


        for event in py.event.get():
            if event.type == py.QUIT:
                run =False

        keys = py.key.get_pressed()

        if keys[py.K_LEFT] and oyuncu.x > 0:       
         oyuncu.x -= oyuncu_hızı
        if keys[py.K_RIGHT] and oyuncu.x < 670:
            oyuncu.x += oyuncu_hızı
        if keys[py.K_UP] and oyuncu.y > 0:
            oyuncu.y -= oyuncu_hızı
        if keys[py.K_DOWN] and oyuncu.y < 490:
            oyuncu.y += oyuncu_hızı



            for düşman in düşmanlar:
                düşman.move(düşman_hızı)


                main()