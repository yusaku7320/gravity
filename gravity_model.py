import random
import math
import pandas as pd

def gravity_model(population1,population2,distance):
    G = 1 #重力定数
    traffic = (G * population1 * population2) / (distance ** 2)
    return traffic

class prefectur():
    def __init__(self,ken):
        self.name = ken[0]
        self.population = ken[1]
        self.distance = {}
        self.traffic = {}
    def __repr__(self):
        return str(self.__dict__)
    def __str__(self):
        return str(self.__dict__)
if __name__ == '__main__':
    list = []
    distance = {}
    ken_list = pd.read_csv("ken.csv")#県のリストを読み込ませる
    distance_list = pd.read_csv("ken_distance.csv")#距離のリストを読み込ませる
    print(ken_list)
    print(distance_list)
    for i in ken_list.values.tolist():#データフレームをリスト型にしてクラス作成
        list.append(prefectur(i))
    for  id,ken in enumerate(list):#リストを東京~千葉でまわす
        for j in distance_list.values.tolist():
            name = j[0]
            distance = j[id+1]
            ken.distance[name] = distance
    for i in list:
        print(i.name)
        print(i.distance)

    for ken1 in list:
        for ken2 in list:
            if ken1.name == ken2.name:
                ken1.traffic[ken2.name] = 0
            else:
                ken1.traffic[ken2.name] = gravity_model(ken1.population,ken2.population,ken1.distance[ken2.name])
    for i in list:
        print(i.name)
        print(i.traffic)
