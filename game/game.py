import pygame as pg
import random
import sys

index = 1

class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)

def check_bound(obj_rct, scr_rct):
    tate = +1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return tate

def main():
    global index

    clock = pg.time.Clock()

    scr = Screen("避けろ!こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (200, 400))
    kkt.update(scr)

    count = 0

    while index:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    index = 2
                    #kkt.rct.centery -= 100
                    if check_bound(kkt.rct, scr.rct) != +1:  
                        index = 0
        
        if index == 1:
            kkt.rct.centery += 1
        elif index == 2:
            kkt.rct.centery -= 1
            count += 1
            if count == 100:
                count = 0
                index = 1
        if check_bound(kkt.rct, scr.rct) != +1:
            index = 0

        kkt.update(scr)

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()