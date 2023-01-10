import pygame as pg
import random
import sys

index = 1       #進行状態の管理

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
    global index        #indexをグローバル変数で定義する

    clock = pg.time.Clock()

    scr = Screen("避けろ!こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (200, 400))
    kkt.update(scr)

    count = 0       #ジャンプ時間を管理する変数

    while index:        #indexが正ならループ
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:        #キーが押されたとき
                if event.key == pg.K_SPACE:     #押されたキーがスペースのとき
                    index = 2       #indexを2にする
        
        if index == 1:      #indexが1の時
            kkt.rct.centery += 1        #自機のy座標に1を足す
        elif index == 2:    #indexが2の時
            kkt.rct.centery -= 1        #自機のy座標から1を引く
            count += 1      #countに1を足す
            if count == 100:        #countが100の時
                count = 0       #countを0にする
                index = 1       #indexを1にする

        if check_bound(kkt.rct, scr.rct) != +1:     #画面外に自機が出ていないか確認する関数を呼び出し、外に出ていたならば
            index = 0       #indexを0にする

        kkt.update(scr)

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()