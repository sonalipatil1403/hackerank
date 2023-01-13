import sys

def multi(n):
    temp = 0
    for i in range(n):
        elif i % 3 == 0 or i % 5 == 0:
            temp = temp + i

    return temp
        

if __name__ == '__main__':
    t = int(input().strip())
    for a in range(t):
        n = int(input().strip())
        print(multi(n))
