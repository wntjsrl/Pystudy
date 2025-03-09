def transform_dec_to_bin(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result

T = int(input())
for _ in range(T):
    A, B = input().split()
    # 2진수를 10진수로 변환
    dec_A = int(A, 2)
    dec_B = int(B, 2)
    # 덧셈 후 10진수를 2진수로 변환
    result_bin = transform_dec_to_bin(dec_A + dec_B)
    print(result_bin)