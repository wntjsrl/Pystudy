# 생성자를 통해 생성된 어떤 수를 반환하는 함수
def calculate_sum(number):
    return number + sum(map(int, str(number)))

# self_number_list를 수정할 함수
def find_self_number():
    for i in range(1, 10001):
        certain_number = calculate_sum(i)
        if certain_number <= 10000:
            self_number_list[certain_number] = False

# True면 셀프 넘버, False면 생성자 있음
self_number_list = [True] * 10001
find_self_number()
for i in range(1, 10001):
    if self_number_list[i]:
        print(i)