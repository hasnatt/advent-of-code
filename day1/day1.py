numbers_list = [int(line.rstrip()) for line in open('input.txt')]

for i in range(0, len(numbers_list)):
    for j in range(i, len(numbers_list)):
        if(numbers_list[i]+numbers_list[j] == 2020):
            print(f' Line {i}: {numbers_list[i]}')
            print(f' Line {j}: {numbers_list[j]}')
            print(f' i + j = {numbers_list[i]+numbers_list[j]}')
            print(f' i * j = {numbers_list[i]*numbers_list[j]}')