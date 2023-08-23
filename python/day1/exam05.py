data=list(range(1,10))
print(data)

data2=data[0:5]
print(data)
print(data2)
print(data[5:8])
print(data[:3])
print(data[3:]) # print(data[3:len(data)])
print(data[:])

print(data)
#data2=data
data2=data[:]
print(data2)
data2[0]=100
print('data',data,id(data))
print('data2',data2,id(data2))

print(data[5:len(data)])
print(data[5:-1]) #-1 앞에 len(data) 생략되어 있다고 생각 => print(data[5:len(data)-1])
#defailt 리스트명 [시작=0, 종료=len(list):간격 = 1)
print(data[2:8:2])
print(data[2::2])
print(data[8:2:-2])
# print(data[len(data)]-1:0:-1)
print(data[::-1])

# print('data: ',data)
# data[15]=100
# print('data: ',data)

# data[2:5] = [100,200,300]



# 배열의 length 가 바뀜
# data[2:5] = [100]
# data[2:5] = [100,200,300,400,500]
data[2:6:2]=[10,20]
print('data: ',data)

# 데이터 지우기
# del data[2:3] #2번지 지우기
del data[2:5] #2-4번지 지우기
print('data',data)