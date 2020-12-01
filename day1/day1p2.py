
numbers_list = []
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]
    numbers_list = lines

for i in range(0, len(numbers_list)): 
    numbers_list[i] = int(numbers_list[i]) 


print(numbers_list)

for i in range(0, len(numbers_list)):
    for j in range(i, len(numbers_list)):
        for k in range(j, len(numbers_list)):
            sum_ijk = numbers_list[i]+numbers_list[j]+numbers_list[k]
            if(sum_ijk == 2020):

                print(f' Line {i}: {numbers_list[i]}')
                print(f' Line {j}: {numbers_list[j]}')
                print(f' Line {k}: {numbers_list[k]}')


                print(f' i + j + k = {sum_ijk}')
                print(f' i * j * k = {numbers_list[i]*numbers_list[j]*numbers_list[k]}')