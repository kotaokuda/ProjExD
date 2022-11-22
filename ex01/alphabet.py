import random
import datetime

ALP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W" ,"X", "Y", "Z"]
num = 2

st = datetime.datetime.now()

for i in range(10):
    alp = random.sample(ALP, 10)
    print("対象文字")
    Alp = [str(a) for a in alp]
    Alp = " ".join(Alp)
    print(Alp)
    ran = random.sample(alp, 2)
    question = ""
    for j in alp:
        if j in ran:
            continue
        question = question + j
    que_lis = random.sample(question, 8)
    print("表示文字")
    que_pri = [str(a) for a in que_lis]
    que_pri = " ".join(que_pri)
    print(que_pri)
    print(" ")
    ans_num = input("欠損文字はいくつあるでしょうか:")
    if ans_num == "2":
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
    else:
        print("不正解です。またチャレンジしてください")
        continue
    one = input("1つ目の文字を入力してください:")
    two = input("2つ目の文字を入力してください:")

    if (one == two):
        print("不正解です。またチャレンジしてください")
        continue
    elif (str(one) in ran and str(two) in ran):
        ed = datetime.datetime.now()
        print("正解")
        print("回答時間:" + str((ed - st).seconds) + "秒")
        break
    else:
        print("不正解です。またチャレンジしてください")