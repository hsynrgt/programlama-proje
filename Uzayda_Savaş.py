#OYUNN YAZILIMINA BAŞLANIYOR NE TARZ OYUN OLDUĞUNU SEÇ
#kullanılacak modüller eklendi

import pygame  as py
import os
import random
py.font.init()
#penceresi yazılıyor

GENİŞLİK= 750
YÜKSEKLİK= 600
EKRAN=py.display.set_mode((GENİŞLİK,YÜKSEKLİK))
beklemesuresi = 30

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


def carpisma(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None

class Lazer():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = py.mask.from_surface(self.img)


    def hareket(self,velocity):
        self.y += velocity
        
    def çizmek(self, EKRAN):
        EKRAN.blit(self.img, (self.x,self.y))

    def collision (self, object):
        return carpisma(object, self)

    def off_screen(self, height):
        return not(self.y <= height and self.y >=0)


class Gemi():
    def __init__(self,x,y,sağlık=100):
        self.x=x
        self.y=y
        self.sağlık=sağlık
        self.gemi_img= None
        self.lazer_img = None
        self.lazerler = []
        self.bekleme_suresi_sayaci = 0

    def beklemesuresi(self):
        if self.bekleme_suresi_sayaci >= beklemesuresi:
           self.bekleme_suresi_sayaci = 0
        else:
            self.bekleme_suresi_sayaci += 1   

    
    def ates(self):
        if self.bekleme_suresi_sayaci == 0:
            lazer = Lazer(self.x, self.y, self.lazer_img)
            self.lazerler.append(lazer)

    def hareket_lazerler(self, velocity, object):
        self.beklemesuresi()
        for lazer in self.lazerler:
            lazer.hareket(velocity)
            if lazer.off_screen(YÜKSEKLİK):
                self.lazerler.remove(lazer)
            elif lazer.collision(object):
                object.sağlık -= 10
                self.lazerler.remove(lazer)

    def çizmek(self, EKRAN):
        EKRAN.blit(self.gemi_img, (self.x,self.y))
        for lazer in self.lazerler:
            lazer.çizmek(EKRAN)


        

    def get_widht(self):
            return self.ship_img.get_widht()

    def get_height(self):
                return self.ship_img.get_height()

class OyuncuGemisi(Gemi):


    def __init__(self,x,y,sağlık=100):
        super().__init__(x,y,sağlık)
        self.gemi_img = GOREV_GEMİSİ
        self.lazer_img = OYUNCU_LAZER
        self.mask = py.mask.from_surface(self.gemi_img)
        self.max_sağlık = sağlık


    def ates(self):
        if self.bekleme_suresi_sayaci == 0:
            lazer = Lazer(self.x+20, self.y, self.lazer_img)
            self.lazerler.append(lazer)

    def hareket_lazerler(self, velocity, objects):
        self.beklemesuresi()
        for lazer in self.lazerler:           
            lazer.hareket(velocity)
            if lazer.off_screen(YÜKSEKLİK):
                self.lazerler.remove(lazer)
            else:
                for object in objects:
                    if lazer.collision(object):
                        objects.remove(object)
                        if lazer in self.lazerler:
                            self.lazerler.remove(lazer)

    def can_barı(self, EKRAN):
        py.draw.rect(EKRAN, (255,0,0), (self.x, self.y + self.gemi_img.get_height(),
                                        self.gemi_img.get_width(), 7))

        py.draw.rect(EKRAN, (0,255,0), (self.x, self.y + self.gemi_img.get_height(),
                                        int (self.gemi_img.get_width() * (self.sağlık/self.max_sağlık)), 7))

    def çizmek(self, EKRAN):
        EKRAN.blit(self.gemi_img, (self.x,self.y))
        self.can_barı(EKRAN)
        for lazer in self.lazerler:
            lazer.çizmek(EKRAN)





class DüşmanGemisi(Gemi):
    RENK_HARİTASI = {
        "red"  : [KIRMIZI_DÜŞMAN_GEMİSİ, LAZER01],
        "green"  :[YEŞİL_DÜŞMAN_GEMİSİ, LAZER02],
        "blue"  :[MAVİ_DÜŞMAN_GEMİSİ, LAZER03]
}

    def __init__(self,x,y,renk,sağlık=100):
         super().__init__(x,y,sağlık)
         self.gemi_img, self.lazer_img = self.RENK_HARİTASI[renk]
         self.mask = py.mask.from_surface(self.gemi_img)

    def move(self, hızı):
        self.y += hızı
    
    def ates(self):
        if self.bekleme_suresi_sayaci == 0:
            lazer = Lazer(self.x-1, self.y, self.lazer_img)
            self.lazerler.append(lazer)


def main():
    run = True
    FPS= 75
    düşmanlar = []
    düşman_hızı = 1
    lazer_hızı = 5
    düşman_uzunluk = 0
    seviye = 0

    main_font=py.font.SysFont("Algerian",30)
    lost_font=py.font.SysFont("Algerian",90)
    

    oyuncu_hızı = 5

    clock = py.time.Clock()


    oyuncu = OyuncuGemisi(350,450)
    lost=False
    lost_count=0


    def çizmek():
        EKRAN.blit(BG, (0,0))
        oyuncu.çizmek(EKRAN)
        seviye_etiketi=main_font.render("SEVİYE: {}".format(seviye),1,(255,255,0))
        EKRAN.blit(seviye_etiketi,(600,10))


        for düşman in düşmanlar:
            düşman.çizmek(EKRAN)

        if lost:
            lost_label = lost_font.render("GAME OVER!" , 1 , (200,0,0))
            EKRAN.blit(lost_label,(int(GENİŞLİK/2-(lost_label.get_width()/2)),int(YÜKSEKLİK/2-(lost_label.get_height()/2))))

        py.display.update()


    while run:
        clock.tick(FPS)
        çizmek()

        if oyuncu.sağlık <= 0:
            lost = True
            if lost:
                lost_count+=1
                if lost_count>= FPS*3:
                    run = False
                else:
                    continue

        if len(düşmanlar) == 0:
            düşman_hızı += 1
            lazer_hızı += 1
            düşman_uzunluk += 5
            seviye += 1
            global beklemesuresi
            beklemesuresi -=5

            for i in range(düşman_uzunluk):
                düşman = DüşmanGemisi(random.randrange(1,700), random.randrange(-1500,-100),random.choice(["red","blue","green"])) 
                düşmanlar.append(düşman)


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
        if keys[py.K_DOWN] and oyuncu.y < 470:
            oyuncu.y += oyuncu_hızı
        if keys [py.K_SPACE]:
            oyuncu.ates()
           

        for düşman in düşmanlar:
            düşman.move(düşman_hızı)
            düşman.hareket_lazerler(lazer_hızı, oyuncu)
            if random.randrange(0, 2*60) == 1:
               düşman.ates()

        
            if carpisma(düşman, oyuncu):
                oyuncu.sağlık -= 10
                düşmanlar.remove(düşman)

            if düşman.y > YÜKSEKLİK:
                düşmanlar.remove(düşman)


        oyuncu.hareket_lazerler(-lazer_hızı, düşmanlar)

def main_menu():
    title_font = py.font.SysFont("Algerian", 50)
    run = True
    while run:
        EKRAN.blit (BG, (0,0))
        main_text = title_font.render("BAŞLAMAK İÇİN FAREYE TIKLAYINIZ", 1, (255, 255, 255))
        EKRAN.blit(main_text, (GENİŞLİK/2 - main_text.get_width()/2, YÜKSEKLİK/2 - main_text.get_height()/2))
         
         
        py.display.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                main()
        
    py.quit()
        



main_menu()