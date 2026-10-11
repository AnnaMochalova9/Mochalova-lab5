N = int(input("Введите количество чисел: "))
max_raznost = -100000
a = []
for i in range(N):
    a.append(int(input("")))
print(a)
for i in range(N):
    for j in range(i+3, N):
        if a[i] < a[j]:
            nov_raznost = a[j] - a[i]
            if nov_raznost > max_raznost:
                max_raznost = nov_raznost
if max_raznost == -100000:
    print("нет таких пар")
else:
    print("Максимальная разность: ", max_raznost)
