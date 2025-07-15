# input
N, M = map(int, input().split())

# 집합으로 받으면 탐색이 O(1)
arr_set = set(input() for _ in range(N))
arr2 = set(input() for _ in range(M))

# 교집합을 구하고 정렬
common = sorted(arr_set & arr2)

# 출력
print(len(common))
for name in common:
    print(name)
