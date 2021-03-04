import time
class Sukudo:
    def __init__(self):
        #构造一个9*9的棋盘
        self.sukudoBoard = [[0]*9 for i in range(9)]
        #同过启发式的搜索查找满足条件的数字填充方式
        res = self.setSukudoBoard(0,0)
        if res is True:
            self.printSukudoBoard()
        else:
            print("NO satisfy answer!")

    def printSukudoBoard(self):
        for i in range(9):
            for j in range(9):
                print('{0}'.format(self.sukudoBoard[i][j]),end='  ')
            # print('\n')
            print('')


    def checkVaild(self,i,j,var):
        #检测在i行第j列放置的var是否满足条件
        for k in range(9):
            #检测数字所在的行有没有出现
            if k!=j and self.sukudoBoard[i][k] == var:
                return False
            #检测数字所在的列是否出现重复
            if k!= i and self.sukudoBoard[k][j] == var:
                return False
        #找到对应的3*3的格子，产看数字是否产生重复
        subX = int(i/3) *3
        subY = int(j/3) *3
        for p in range(subX,subX+3):
            for q in range(subY,subY+3):
                if p!=i and q!=j and self.sukudoBoard[p][q] == var:
                    return False
        return True

    def setSukudoBoard(self,x,y):
        #使用启发式探索填充棋盘
        if  y >= 9:
            y = 0
            x += 1
        if x >= 9:
            return True

        #从给定位置从1到9九个数字中选取一个满足条件的来填充
        for var in range(1,10):
            #检测数字是否符合条件
            if self.checkVaild(x,y,var) is True:
                self.sukudoBoard[x][y] =var
                #设置下一个数字的位置
                self.printSukudoBoard()
                if self.setSukudoBoard(x,y+1) is True:
                    return True
                print("********************************")
                time.sleep(1)

            #当前位置找不到合适的数字填充，返回上一部
        self.sukudoBoard[x][y] = 0
        return  False

if __name__ == '__main__':
    s = Sukudo()


#
# print([[0]*9 for i in range(9)])