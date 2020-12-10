def lines():
    return [line.rstrip() for line in open('input.txt')]

# part1
def find_seat_value(seat):
    # this imitates binary
    row_id = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    col_id = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
    seat_number = row_id * 8 + col_id
    return seat_number


# part 2
def find_my_seat(passes):
    # passes = passes.sort()
    passes = sorted(passes) 
    z = [x for x in range(passes[0], passes[-1]+1) if x not in passes] 
    return(z[0])                         

if __name__ == '__main__':
    # part 1 implementation
    passes = lines()
    max_pass = []
    for i in passes:
        max_pass.append(find_seat_value(i))
    print(f'Part 1: {max(max_pass)}')

    # part 2 implementation
    print(f'Part 2: {find_my_seat(max_pass)}')

