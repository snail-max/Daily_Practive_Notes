# -*-coding:utf-8-*-
        #用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
        #name=[‘alex’,’wupeiqi’,’yuanhao’,’nezha’]





name = ["alex","wupeiqi","yuanhao","nezha"]
name_sb = map(lambda x:x+"_"+"sb",name)
for i in range(len(name)):
    print(name_sb.__next__())
