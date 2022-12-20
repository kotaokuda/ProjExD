import math
import random
import sys

import pygame as pg


#敵の弾の最大数
ENEMY_MAX = 100


class Screen:
    def __init__(self, title, wh , img_path):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy      #900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]        
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:
    def __init__(self, clo, herh, v, scr:Screen):
            self.sfc = pg.Surface((2 * herh, 2 * herh)) # 正方形の空のSurface
            self.sfc.set_colorkey((0, 0, 0))
            pg.draw.circle(self.sfc, clo, (herh, herh), herh)
            self.rct = self.sfc.get_rect()
            self.rct.centerx = random.randint(0, scr.rct.width)
            self.rct.centery = random.randint(0, scr.rct.height)
            self.vx = v[0]
            self.vy = v[1]

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        scr.sfc.blit(self.sfc, self.rct)


#敵の弾を飛ばすクラス
class EnemyShot:
    #定義を行う(xは最初のx座標の位置、yは最初のy座標の位置、aは角度、spは速度)
    def __init__(self, x, y, a, sp):
        #半径が15の弾を作成する
        self.sfc = pg.Surface((30, 30))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, "red", (15, 15), 15)
        self.rct = self.sfc.get_rect()
        #self.xをx座標で初期化する
        self.x = x
        #self.yをy座標で初期化する
        self.y = y
        #self.vを速度で初期化する
        self.v = sp
        #self.radを角度で初期化する
        self.rad = a
        #self.vxを横の移動距離で初期化する
        self.vx = self.v * math.cos(math.radians(self.rad))
        #self.vyを縦の移動距離で初期化する
        self.vy = self.v * math.sin(math.radians(self.rad))
    
    #表示を行う
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        #self.x(x座標)の位置を更新する
        self.x = self.x + self.vx
        #self.y(y座標)の位置を更新する
        self.y = self.y + self.vy
        #表示を行う
        scr.sfc.blit(self.sfc, [self.x, self.y])
            


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """

    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()

    #弾を管理する番号を0で初期化する
    emy_no = 0
    #弾が存在しているかを管理するリストを作成する
    emy_f = [False] * ENEMY_MAX
    #弾を格納するリストを作成する
    emy_lst = [] * ENEMY_MAX

    scr = Screen("逃げろ!こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (900, 400))
    kkt.update(scr)

    bkd_lst = []
    for _ in range(5):
        bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
        bkd_lst.append(bkd)

    while True:
        scr.blit()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        for i in range(5):
            bkd_lst[i].update(scr)
            if kkt.rct.colliderect(bkd_lst[i].rct):
                return
        
        #500回画面が更新されたとき
        if pg.time.get_ticks() % 500 == 0:
            #5回ループする
            for i in range(5):
                #無限ループする
                while True:
                    #emy_f[emy_no]がFalseのとき
                    if not emy_f[emy_no]:
                        #emy_f[emy_no]をTrueにする
                        emy_f[emy_no] = True
                        #弾を作成する
                        emy = EnemyShot(random.randint(0 ,1600), 1, random.randint(60, 120), 1)
                        #弾をemy_lstにいれる
                        emy_lst.insert(emy_no, emy)
                        #ループを抜ける
                        break
                    #emy_noを更新する
                    emy_no = (emy_no + 1) % ENEMY_MAX

        #弾の上限回ループする
        for i in range(ENEMY_MAX):
            #emy_fがTrueのとき
            if emy_f[i]:
                #emy_lit[i]を更新する
                emy_lst[i].update(scr)
                #弾が画面外に出た時
                if ((emy_lst[i].__dict__)["x"] < 0 or (emy_lst[i].__dict__)["x"] > 1600 or (emy_lst[i].__dict__)["y"] > 900):
                    #弾を消す
                    emy_f[i] = False

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()