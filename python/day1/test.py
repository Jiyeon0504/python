
'''
정수 2개를 입력받아 사칙연산의 결과 출력
'''

print('첫번째 정수를 입력 :', end='')
num01 = int(input())
#print(type(num01))
print('두번째 정수를 입력 :', end='')
num02 = int(input())

# print(num01,'+', num02,'=', sep=':')
print(num01,'+', num02,'=', num01+num02)
print('%d - %d = %d' %(num01,num02,num01-num02))
print('%d * %d = %d' %(num01,num02,num01*num02))
print('%d / %d = %d' %(num01,num02,num01/num02))

print('{0} / {1} = {2}'.format(num01,num02,num01/num02))
print(f'{num01}/{num02} = {num01/num02}')
print(f'{num01}/{num02} = {num01//num02}')
print(f'{num01}%{num02} = {num01%num02}')
print(2**3)

