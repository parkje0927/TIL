
## 반복문(for, while)

a = range(10)
print(list(a))
print()

for i in range(10):
    print(i)
print()

for i in range(10, 0, -2):
    print(i)
print()

i = 1
while i <= 10:
    print(i)
    i = i + 1
print()

i = 10
while i >= 1:
    print(i)
    i = i -1
print()

i = 1
while(True):
    print(i)
    if i == 5:
        break
    i = i + 1
print()

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print()