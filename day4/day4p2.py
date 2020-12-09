import re
KEYS = {'ecl', 'pid', 'eyr', 'hcl', 'byr','iyr', 'hgt'}

def read_lines():
    return open("input.txt").read().split("\n\n")

def part1():
    lines = read_lines()
    count = 0 
    for i in range(0,len(lines)):
        passports = lines[i].replace('\n', ' ').split()
        passports = dict([fields.split(':') for fields in passports])

        if passports.keys() >= KEYS:
            count+=1
    return(count) 

def part2():
    lines = read_lines()


    for i in range(0,len(lines)):
        passports = lines[i].replace('\n', ' ').split()
        passports = dict([fields.split(':') for fields in passports])

        height = int(re.sub('\D', '', passports['hgt']))  
        # print(re.sub('[0-9]', '', passports['hgt']))

        if passports.keys() >= KEYS:
            if not int(passports['byr']) >= 1920 and int(passports['byr']) <= 2002:
                return()
            if not int(passports['iyr']) >= 2020 and int(passports['iyr']) <= 2002:
                return()
            if re.sub('[0-9]', '', passports['hgt']) == 'cm':
                if height < 150 and height > 193:
                    return()
            elif re.sub('[0-9]', '', passports['hgt']) == 'in':
                if height < 59 and height > 76:
                    return()
            
                
 



print(part2())


# print(part1())
    

  

