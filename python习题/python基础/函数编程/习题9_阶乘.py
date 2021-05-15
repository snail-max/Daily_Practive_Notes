# -*-coding:utf-8-*-




def factorial(n):
    sum = 1
    for i in range(2,n+1):
        print(i)
        sum = sum * (i-1)
    else:
        print(sum)
        return sum

if __name__ == '__main__':
    factorial(10)





