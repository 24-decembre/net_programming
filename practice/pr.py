'''
print(10+20)
print('사물인터넷')
print("abc" * 3)

x = 25
y = 32
z = x+y
print(x, y)
print(x, '+', y, "=", z)

n = input('type a number: ')

n = int(n)

print(n)

print(type(n))
'''

# score = int(input("type your score: "))
# res = 'pass' if score >= 90 else 'fail'
# print(res)
'''
n = int(input("type int number: "))
if n>0 :
    print("positive")
else:
    if n<0:
        print("negative")
    else:
        print("0")
'''
'''
# 1부터 100까지 더하기
sum = 0
for i  in range(1, 101, 1):
    sum = sum + i

print("sum = ", sum)
'''
'''
print('123'.isdigit())
print('abcABC'.isalpha())
print('abc123'.isalnum())
print('AB'.isupper())
print('ab'.islower())
print(' '.isspace())

str = 'Python programming is easy'
print(str.upper())
print(str.lower()) 
print(str.swapcase()) #대소문자 바꾸기
print(str.title()) #첫글자만 대문자로 변환
'''

str = ' hello '
print(str.strip()) #공백 제거
print(str)
print(str.lstrip()) #왼쪽 공백 제거
