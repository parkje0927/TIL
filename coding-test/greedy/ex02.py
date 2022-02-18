# 큰 수의 법칙

## 입력 받기
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

## 내림차순
data.sort(reverse=True)

first = data[0]
second = data[1]
result = 0

## 가장 큰 수를 K 만큼 더하기
## 두 번째로 큰 수 더하는데, 큰 수 == 작은 수 이면 K 만큼 더하고,
## 큰 수 > 작은 수면 1번만 더하고 다시 큰 수는 K 만큼 더한다.
number = 0
while True:
    for i in range(k):
        result += first
        m -= 1
        if (m == 0):
            break
    
    if first > second:
        result += second
        m -= 1
        if (m == 0):
            break
        
    elif first == second:
        for j in range(k):
            result += second
            m -= 1
            if (m == 0):
                break
    
print(result)

# 다른 풀이

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

count = int(m / (k + 1)) * k
count += (m % (k + 1))

result = 0
result += count * first
result += (m - count) * second

print(result)