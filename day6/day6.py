def lines():
    lines = [x.replace("\n", "") for x in open("input.txt").read().split("\n\n")]
    return(lines)

def lines_2():
    lines = [x.split("\n") for x in open("input.txt").read().split("\n\n")]
    return(lines)

def split(word): 
    return [char for char in word]     

if __name__ == "__main__":
    sumcount = 0
    for question in lines():
        sumcount += len("".join(set(question)))
    
    sumcount2 = 0
    for question in lines_2():
        i = [set(split(words)) for words in question]
        sumcount2 += len(set.intersection(*i))

    print(f'Part 1 sum : {sumcount}') 
    print(f'Part 2 sum : {sumcount2}') 



