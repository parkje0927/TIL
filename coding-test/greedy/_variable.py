
# 변수명 정하기
# - 영문과 숫자, _로 이루어진다.
# - 대소문자를 구분한다.
# - 문자나 _ 로 시작한다.
# - 특수문자를 사용하면 안 된다.
# - 키워드를 사용하면 안 된다.

a = 1
print(a)
A = 2
print(a, A)

a, b, c = 3, 2, 1
print(a, b, c)

a, b = 10, 20
a, b = b, a 
print(a, b)

a = 1234
print(type(a))

print(a, b, c, sep=', ')

print(a, end=' ')
print(b, end = ' ')