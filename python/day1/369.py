import random

num=random.randint(20,50)
print(num)


# r=random.randint(20,50)
# print(r)

# for r in range(1,r):
#
#     if r%10==0:
#         if(r//10)%3==0:
#             print(r,'뽀'*(r//10),'숑짝',sep='')
#         else:
#             print(r,'뽀'*(r//10),'숑',sep='')
#
#
#     else:
#         if r//10>1 and (r//10)%3==0:
#             if (r%10 == 3) or (r%10 == 6) or (r%10 == 9):
#
#                 print(r,'짝짝')
#
#             else:
#                 print(r,'짝')
#         else:
#             if (r%10 == 3) or (r%10 == 6) or (r%10 == 9):
#                 print(r,'짝')
#             else:
#                print(r)


# 교수님 풀이
for i in range(1,num+1):
    n1 = i%10
    n10 = i//10

    # print(i, end=' ')
    print(f'{i<3}', end='')
    # if n1 ==3 or n1 ==6 or n1==9:
    if not n1:
        print('뽀'* n10,'쑝', end='',sep='')
    if n1 in [3,6,9]:
        print('짝', end='')
    if n10 in [3,6,9]:
        print('짝', end='')
    print()



