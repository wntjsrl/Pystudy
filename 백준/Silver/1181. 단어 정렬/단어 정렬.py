# input
N = int(input())
my_set = {input() for _ in range(N)}
arr = list(my_set)

my_arr = [None] * len(arr)

for i in range(len(arr)):
    my_arr[i] = [i, len(arr[i])]

# 정렬
my_arr.sort(key=lambda x: (x[1], arr[x[0]]))

for i in range(len(my_arr)):
    print(arr[my_arr[i][0]])
