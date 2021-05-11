# -*-coding:utf-8-*-
"""
3、写代码，有如下列表，按照要求实现每一个功能
    li＝[‘alex’, ‘eric’, ‘rain’]
    计算列表长度并输出
    列表中追加元素“seven”，并输出添加后的列
    请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
    请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
    请删除列表中的元素“eric”，并输出修改后的列表
    请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
    请删除列表中的第3个元素，并输出删除元素后的列表
    请删除列表中的第2至4个元素，并输出删除元素后的列表
    请将列表所有的元素反转，并输出反转后的列表
    请使用for、len、range输出列表的索引
    请使用enumrate输出列表元素和序号（序号从100开始）
    请使用for循环输出列表的所有元素
"""

def operatelist(lis):

    # 计算列表的长度
    leng = 0
    for i in lis:
        leng += 1
    assert leng == len(lis)
    print("列表{}的长度是{}".format(str(lis),leng))

    lis.append('seven')
    print('追加元素%s: '%(lis))

    # 插入元素
    lis.insert(1,'Tony')
    print(lis)
    # 修改元素
    lis[2] = 'Kelly'
    print(lis)
    # 删除元素
    delelement = lis.pop(2)
    print(delelement,lis)
    print(lis.remove("rain"))
    # 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
    # print(lis.pop(2))
    # print(lis)

    # 请删除列表中的第2至4个元素，并输出删除元素后的列表
    # print(lis.remove(2))
    del lis[2:4]
    print(lis)

    # 请将列表所有的元素反转，并输出反转后的列表
    print(lis.reverse())

    #请使用for、len、range输出列表的索引
    for i in lis:
        print(i)
    len(lis)-1
    for i in range(len(lis)):
        print(i-1)







if __name__ == '__main__':
    lis = ["alex","eric","rain"]
    operatelist(lis)



