import random
import math
import pandas as pd

def gravity_model():
    pass

class prefectur():
    def __init__(self,ken):
        self.name = ken[0]
        self.population = ken[1]
    def __repr__(self):
        return str(self.__dict__)
    def __str__(self):
        return str(self.__dict__)
    def distance(self,list):
        self.distance_list = list

if __name__ == '__main__':
    list = []
    ken_list = pd.read_csv("ken.csv",encoding="SHIFT-JIS",sep="\t")#県のリストを読み込ませる
    distance_list = pd.read_csv("ken_distance.csv",encoding="SHIFT-JIS",sep="\t")#距離のリストを読み込ませる
    print(ken_list)
    print(distance_list)
    print(a)
    for i in ken_list.values.tolist():#データフレームをリスト型にしてクラス作成
        list.append(prefectur(i))
