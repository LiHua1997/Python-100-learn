#4个空瓶换1瓶，买了7瓶
total = 0
empty = 0
borow = 0
change = 0
num = int(input('买几瓶： '))



for _ in range(num):
    total += 1
    empty += 1
    if empty == 4:
        total += 1
        empty -= 4
        change += 1



print("总共可获得%d瓶，其中兑换了%d瓶，借了%d瓶，剩%d个空瓶子"%(total,change,borow,empty))

