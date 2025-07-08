# input
N = int(input())
arr = list(map(int, input().split()))

# 정렬
arr.sort()

# 계산
min_time = 0
for i in range(N):
    min_time += arr[i] * (N - i)

# 결과
print(min_time)
