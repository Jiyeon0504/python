# print("hello"/1)
# data[]= input()
#
# type(i) == type(int)

data = input('데이터를 입력하세요').split()
print(data)

# 데이터 뽑아내기
# for numStr in data :
#     num = int(numStr)
#     for numStr in data:
#         for i in range(2,int(numStr)):
#             if int(numStr) % i ==0:
#                 cnt=cnt+1
#         if cnt==0:

    # for numStr in data:
    #     if numStr.isdigit():
    #         num=int(numStr)
    #

    num = 25
    i=2
    while i <num and num % i: #순서가 바뀌면 안됨. 이 순서 여야함
        i += 1
    print('소수' if i == num else '비소수')
