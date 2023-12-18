from random import randint
 
# Бинарный поиск

# Создание списка, его сортировка по возрастанию

a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)
 
# искомое число
value = int(input())
 
mid = len(a) // 2
low = 0
high = len(a) - 1
 
while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print("No value")
else:
    print("ID =", mid)