# -*-coding:utf-8-*-
# 用递归实现2分查找的算法，以从列表 a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107] 查找指定的值。


a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107]



def dichotomy(start,end,lis,num):
    if start < end:
        mid = (start+end)//2
        if num > lis[mid]:
            start = mid+1
            end = len(lis)
            dichotomy(start,end,lis,num)
        elif num < lis[mid]:
            start = 0
            end = mid-1
            dichotomy(start, end, lis, num)
        else:
            print(num)
            return num
    else:
        print("没有这个数")
        return None




if __name__ == '__main__':
    a = [1, 3, 4, 6, 7, 8, 9, 11, 15, 17, 19, 21, 22, 25, 29, 33, 38, 69, 107]
    start = 0
    end = len(a)
    dichotomy(start, end, a, 25)











