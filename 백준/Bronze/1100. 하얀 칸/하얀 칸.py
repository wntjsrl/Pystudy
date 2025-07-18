# input
arr = [list(input()) for _ in range(8)]

# 계산
cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 and arr[i][j] == "F":
                cnt += 1
        else:
            if j % 2 == 1 and arr[i][j] == "F":
                cnt += 1

# 결과 출력
print(cnt)
