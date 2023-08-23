# import random
# r=int(random.random()*10)
# # print(int(random.random() *10)) 위에랑 같은 코드
# print(r)
#
# if r%2 ==0 :
#     print(f'{r} :짝수')
# else:
#     print(f'{r}: 홀수')


num=int(input('정수입력: '))

if num <0:
    print(f'{num} :음수입니다')
elif num %2==0:
    print(f'{num} :짝수입니다')
else:
    print(f'{num} :홀수입니다')


num=int(input('정수입력: '))

if num >0:
    if num%2 :
    print(f'{num} :짝수입니다')
    else:
    print(f'{num} :홀수입니다')
else:
    print(f'{num} :음수입니다')



# if num : # 이 경우는 음의 값도 참이 된다
#     if num%2 :
#     print(f'{num} :짝수입니다')
#     else:
#     print(f'{num} :홀수입니다')
# else:
#     print(f'{num} :짝/홀 판단은 양수만 가능합니다')


if num<0:
    print('짝/홀 판단은 양수만 가능합니다')
elif num%2:
    print(num, ':홀수')
else:
    print(num, ':짝수')