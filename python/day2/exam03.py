# 1~100 사이의 정수 10개를 원소로 가지는 리스트 data 선언


#방법 2
#data = list()
# for i in range(10):
#     data.append(i+1)

#방법3
data = [i+1 for i in range(10)]
print(data)

# 홀수만 집어넣기
# data = [i+1 for i in range(10) if (i+1)%2]
# print(data)

data = [2*i+1 for i in range(5)]
print(data)


# 구구단 데이터 생성
dan = 4
guguData=[dan*i for i in range(1,10)]
print(guguData)

#2~9단 값
guguData=[dan*i for dan in range(2,10) for i in range(1,10)]
print(guguData)


#글자수세서 데이터 추출
strData=['hello','good','bye','welcome','apple','sorry']
fiveStrData=[s for s in strData if len(s)==5]
print(fiveStrData)

copyStrData=strData[:]
copyStrData2=strData.copy()


print('strData: ', strData,id(strData))
print('copyStrData: ',copyStrData, id(copyStrData))
print('copyStrData: ',copyStrData2, id(copyStrData2))


# 밑에 코드로 하면 에러남 (튜플은 추가 할 수 없어서)
# tupleData = tuple()
# tupleData.__add__(10)
# print(tupleData)



