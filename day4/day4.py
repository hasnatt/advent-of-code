lines = open("input.txt").read().split("\n\n")


for i in range(0,len(lines),100):
    print(f"i = {i}")
    print(lines[i])
    print('\n')

    l =  [line.rstrip(':') for line in lines[i]]
    print(l)


