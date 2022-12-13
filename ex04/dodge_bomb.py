import pygame as pg
import sys
import random
<<<<<<< HEAD

ENEMY_MAX = 100
emy_no = 0
emy_f = [False] * ENEMY_MAX
emy_x = [0] * ENEMY_MAX
emy_y = [0] * ENEMY_MAX
emy_a = [0] * ENEMY_MAX
=======
import math

#爆弾の最大数
ENEMY_MAX = 100
#爆弾を区別するための変数
emy_no = 0
#爆弾が定義されたかを管理するリストをENEMY_MAXの要素数で、Falseで初期化する
emy_f = [False] * ENEMY_MAX
#爆弾のx座標を管理するリストをENEMY_MAXの要素数で0で初期化する
emy_x = [0] * ENEMY_MAX
#爆弾のy座標を管理するリストをENEMY_MAXの要素数で0で初期化する
emy_y = [0] * ENEMY_MAX
#爆弾の角度を管理するリストをENEMY_MAXの要素数で0で初期化する
emy_a = [0] * ENEMY_MAX
#爆弾のスピードを管理するリストをENEMY_MAXの要素数で0で初期化する
emy_speed = [0] * ENEMY_MAX
>>>>>>> add_func

def check_bound(obj_rct, scr_rct):
    #第1引数:こうかとんrectまたは爆弾rect
    #第2引数:スクリーンrect
    #範囲内: +1 / 範囲外: -1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

<<<<<<< HEAD
def set_enemy(x, y, a):
    global emy_no
    while True:
        if emy_f[emy_no] == False:
            emy_f[emy_no] = True
            emy_x[emy_no] = x
            emy_y[emy_no] = y
            emy_a[emy_no] = a
            break
    emy_no = (emy_no + 1) % ENEMY_MAX
=======
#爆弾を定義する
def set_enemy(x, y, a, sp):
    #xが爆弾のx座標、yが爆弾のy座標、aが爆弾の角度、spが爆弾のスピード
    #emy_noを変更するため、グローバル宣言をする
    global emy_no
    #emy_f[emy_no]が定義されていない値になるまでループする
    while True:
        #爆弾が定義されていないとき
        if emy_f[emy_no] == False:
            #爆弾を定義する
            emy_f[emy_no] = True
            #爆弾のx座標にxを代入する
            emy_x[emy_no] = x
            #爆弾のy座標にyを代入する
            emy_y[emy_no] = y
            #爆弾の角度にaを代入する
            emy_a[emy_no] = a
            #爆弾のスピードにspを代入する
            emy_speed[emy_no] = sp
            #ループを抜ける
            break
        #爆弾の番号を次の値に設定する
        emy_no = (emy_no + 1) % ENEMY_MAX
>>>>>>> add_func

def main():
    clock = pg.time.Clock()

<<<<<<< HEAD
=======
    #フレーム数をカウントする変数を0で初期化する
    time = 0
    #mainを抜けるための変数を0で初期化する
    j = 0

>>>>>>> add_func
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    bomb_sfc = pg.Surface((20, 20))     #正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
<<<<<<< HEAD
    bomb_rct.centerx = random.randint(0, scrn_rct.width - 10)
    bomb_rct.centery = random.randint(0, scrn_rct.height - 10)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    vx, vy = +1, +1

    keyys = {pg.K_UP:-1, pg.K_DOWN:+1}
=======
    #bomb_rct.centerx = random.randint(0, scrn_rct.width - 10)
    #bomb_rct.centery = random.randint(0, scrn_rct.height - 10)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    #vx, vy = +1, +1
>>>>>>> add_func

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
    
        key_dct = pg.key.get_pressed()

        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1

        scrn_sfc.blit(tori_sfc, tori_rct)

<<<<<<< HEAD
        yoko , tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)

        if tori_rct.colliderect(bomb_rct):
            return
=======
        #yoko , tate = check_bound(bomb_rct, scrn_rct)
        #vx *= yoko
        #vy *= tate
        #bomb_rct.move_ip(vx, vy)

        #500フレーム経過したら、爆弾を出す
        if time == 500:
            #フレーム数をカウントする変数を0に戻す
            time = 0
            #5回爆弾を定義する
            for i in range(5):
                set_enemy(800, 0, random.randint(60, 120), 1)
        
        #フレーム数をカウントする変数に1を足す
        time += 1

        #爆弾の処理を行う
        for i in range(ENEMY_MAX):
            #emy_noがiの爆弾の移動先を設定する 現在のx座標+スピード*cos(爆弾の角度)
            emy_x[i] = emy_x[i] + emy_speed[i] * math.cos(math.radians(emy_a[i]))
            #現在のy座標+スピード*cos(爆弾の角度)
            emy_y[i] = emy_y[i] + emy_speed[i] * math.sin(math.radians(emy_a[i]))
            #爆弾が定義されているなら
            if emy_f[i] == True:
                #爆弾の表示を行う
                scrn_sfc.blit(bomb_sfc, [emy_x[i], emy_y[i]])
                #爆弾の位置が画面外に出たら
                if (emy_x[i] < 0 or emy_x[i] > 1600 or emy_y[i] > 900):
                    #爆弾の定義を取り消す
                    emy_f[i] = False
            #こうかとんと爆弾の距離が10より近いとき
            if ((int(tori_rct.centerx) - emy_x[i]) * (int(tori_rct.centerx) - emy_x[i]) + (int(tori_rct.centery) - emy_y[i]) * (int(tori_rct.centery) - emy_y[i])) < 1000:
                #mainを抜けるためにjを1に変更する
                j = 1
        
        #jが1の時、mainを抜ける
        if j == 1:
            break

        #scrn_sfc.blit(bomb_sfc, bomb_rct)
>>>>>>> add_func

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()