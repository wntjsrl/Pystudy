# Baekjoon 2729 이진수 덧셈 (2025.03.09)

# import sys

# sys.stdin = open("2729_input.txt", "r")
# sys.stdout = open("2729_my_output.txt", "w")

# def transform_dec_to_bin(result_dec):
#     # 종료 조건
#     if result_dec == 0:
#         return
#     global result
#     # 결과 값 저장
#     result = str(result_dec % 2) + result
#     transform_dec_to_bin(result_dec // 2)
#
# T = int(input())
# for _ in range(T):
#     A, B = input().split()
#     # A 2진수에서 10진수로 변경
#     dec_A = 0
#     for i in range(len(A)):
#         dec_A += (2 ** i) * int(A[len(A) - i - 1])
#     # B 2진수에서 10진수로 변경
#     dec_B = 0
#     for i in range(len(B)):
#         dec_B += (2 ** i) * int(B[len(B) - i - 1])
#     # A + B
#     result_dec = dec_A + dec_B
#     # A + B 10진수에서 2진수로 변경
#     result = ""
#     transform_dec_to_bin(result_dec)
#     print(result)

T = int(input())
for _ in range(T):
    A, B = input().split()
    # 2진수를 10진수로 변환
    dec_A = int(A, 2)
    dec_B = int(B, 2)
    # 덧셈 수행 후 2ㅈ빈수 변환
    result = bin(dec_A + dec_B)[2:]
    print(result)
