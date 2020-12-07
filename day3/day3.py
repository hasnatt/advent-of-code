   
def traverse_paths(right,down)  : 
    paths = [line.rstrip() for line in open('input.txt')]
    width = len(paths[0])
    tree_count = 0
    position = 0

    for i in range(0, height, down):
        path = paths[i].strip()
        if path[position] == '#':

            tree_count += 1
        position += right
        position %= width
    return(tree_count)    

def part2():
    total = traverse_paths(1,1) * traverse_paths(3,1) * traverse_paths(5,1) * traverse_paths(7,1) * traverse_paths(1,2)
    return(total)

print(traverse_paths(3,1))
print(part2())    