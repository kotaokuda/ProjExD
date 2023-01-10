import pygame as pg
import random
import sys


class Screen:#背景を生成
    def __init__(self, title, whtpl, bgfile):
        self.title = title
        self.whtpl = whtpl
        pg.display.set_caption(self.title)
        self.sfc = pg.display.set_mode(self.whtpl)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgfile)
        self.bgi_rct = self.bgi_sfc.get_rect()
 
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:#こうかとんを生成
    def __init__(self, figfile, zoom, center):
        self.sfc = pg.image.load(figfile)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.sfc = pg.transform.flip(self.sfc, True, False) #向きを反転
        self.rct = self.sfc.get_rect()
        self.rct.center = center

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        key_dct = pg.key.get_pressed()
        self.rct.centery += 2
        if key_dct[pg.K_SPACE]:
            for _ in range(7):
                self.rct.centery += -0.1
                if self.rct.top < scr.rct.top:
                    self.rct.centery += 0.1
        scr.sfc.blit(self.sfc, self.rct) # 練習3


class Wall:
    def __init__(self):
        self.top = random.randint(0, 6)
        self.sfc1 = pg.Surface((100, self.top * 100))
        self.sfc1.set_colorkey((0, 0, 0))
        self.sfc2 = pg.Surface((100, 600 - self.top * 100))
        self.sfc2.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc1, (0, 128, 0), (0, 0, 100, self.top * 100), 0)
        pg.draw.rect(self.sfc2, (0, 255, 255), (0, 0, 100, 600 - self.top * 100), 0)
        self.rct1 = self.sfc1.get_rect()
        self.rct1.center = (1550, self.top * 50)
        self.rct2 = self.sfc2.get_rect() 
        self.rct2.center = (1550, 600 + self.top * 50)


    def blit(self, scr):
        scr.sfc.blit(self.sfc1, self.rct1)
        scr.sfc.blit(self.sfc2, self.rct2)

    def update(self, scr):
        self.rct1.move_ip(-1, 0)
        self.rct2.move_ip(-1, 0)
        self.blit(scr)


def main():
    global game
    time = 0
    index = 0       #ゲームの進行を管理する変数

    clock =pg.time.Clock()


    scr = Screen("飛べ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    scr.blit()

    kkt = Bird("fig/3.png", 2.0, (scr.whtpl[0]/2, scr.whtpl[1]/2))
    kkt.blit(scr)

    wlls = [Wall()]
    wlls[0].blit(scr)

    font1 = pg.font.Font(None, 200)     #テキストのフォントおよびサイズの設定
    font2 = pg.font.Font(None, 100)     #テキストのフォントおよびサイズの設定

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
                return
            ##########################################################################################################
            if event.type == pg.KEYDOWN:                                    #キーが押されたとき
                if index == 1:                                              #indexが1の時
                    if event.key == pg.K_x:                                 #押されたキーがxの時
                        game = False                                        #gameをFalseにする
                        return                                              #main関数を抜ける
                    if event.key == pg.K_r:                                 #押されたキーがrの時
                        index = 0                                           #indexを0にする
                        kkt.rct.center = (scr.whtpl[0]/2, scr.whtpl[1]/2)   #こうかとんの位置を初期化する
                        wlls = [Wall()]                                     #壁をリセットする
                        time = 0                                            #タイマーをリセットする
                        pg.display.update()                                 #ディスプレイを更新する
            ###########################################################################################################
        
        if index == 0:      #indexが0の時

            kkt.update(scr)

            if time % 700 == 699:
                    wlls.append(Wall())

            for wll in wlls:
                wll.update(scr)
                if wll.rct1.right < 0:
                    wlls.remove(wll)

                if kkt.rct.colliderect(wll.rct1) or kkt.rct.colliderect(wll.rct2):
                    index = 1
            
            if kkt.rct.bottom > scr.rct.bottom:
                index = 1
        
            pg.display.update()
            time += 1

            ############################################################################################################################
            if index == 1:      #indexが1の時

                text1 = font1.render("GAME OVER!", True, (255, 0, 0))                   #メッセージの文字、滑らかにするかを指定、色を指定
                text2 = font2.render("Finish [X] Restart [R]", True, (255, 255, 255))   #メッセージの文字、滑らかにするかを指定、色を指定
                scr.sfc.blit(text1, (350, 300))                                         #メッセージと、場所を指定して表示
                scr.sfc.blit(text2, (450, 500))                                         #メッセージと、場所を指定して表示

                pg.display.update()     #画面を更新する
            #############################################################################################################################

        clock.tick(1000)


if __name__ == "__main__":
    game = True
    pg.init() # 初期化
    while game:
        main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()