# 왕실의 나이트

input_data =  input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #ord: 문자를 인자로 받아 유니코드 정수를 반환

#나이트 방향 리스트
steps = [(-2,-1) , (-1,-2), (1,-2), (2,-1), (2,1) , (1,2), (-1,2), (-2,1)]

result = 0
for step in  steps:
	next_row  = row + step[0]
	next_column = row + step[1]

	if next_row >=1 and next_row <=8 and  next_column >=1 and next_column <=8:
		result+=1


print(result)


