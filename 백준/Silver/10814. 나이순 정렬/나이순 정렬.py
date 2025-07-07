# input
N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 나이순 정렬
arr.sort(key=lambda x: int(x[0]))

# 결과
for person in arr:
    print(*person)
