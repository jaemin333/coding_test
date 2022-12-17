#떡볶이 떡 만들기(파라메트릭 서치 문제)

n,m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

#이진 탐색 시작점 끝점
start = 0
end = max(array)

result = 0
while(start <= end):
	total = 0
	mid = (start+end) // 2
	for x in array:
		# 잘린 떡 길이 계산
		if x > mid:
			total += x-mid
	#떡의 길이가 부족할 떄
	if total < m:
		end = mid-1

	#떡의 양이 충분한 경우
	else:
		result = mid
		start = mid + 1

print(result)
	

