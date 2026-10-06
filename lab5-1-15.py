N = int(input("введите колличество чисел "))
cnt = 0
n1 = int(input("введите число1 "))
for i in range(N-1):
    nov = int(input("введите число "))
    if (n1 > 0 and nov < 0) or (n1 < 0 and nov > 0):
        cnt += 1
    n1 = nov
print(cnt)
