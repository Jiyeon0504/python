
#
# *
# **
# ***

for i in range(1,6):
    print('*' * i)
print()


for j in range (1,10):
    if j<6:
        print('*' * j)
    else:
        print('*'*(10-j))
print()


for k in range(0,5):
    print(' '*k,'*'*(5-k),sep='')
print()




#교수님 풀이

# for i in range(9):
#     참문장 if 조건식 else 거짓문장
#     print('*'*cnt)


for i in range(9):
    cnt = (i+1) if i<5 else (9-i)
    print('*'*cnt)


