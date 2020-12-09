import re
KEYS = {'ecl', 'pid', 'eyr', 'hcl', 'byr','iyr', 'hgt'}

hcl = re.compile(r'^#([0-9a-f]{6})$')
ecl = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
pid = re.compile(r'^[0-9]{9}$')
hgt = re.compile(r'^([0-9]{2,3})(cm|in)$')


def read_lines():
    return open("input.txt").read().split("\n\n")

def part1(lines):
    part2_list = []
    count = 0 
    for i in range(0,len(lines)):
        passports = lines[i].replace('\n', ' ').split()
        passports = dict([fields.split(':') for fields in passports])

        if passports.keys() >= KEYS:
            count+=1
            part2_list.append(passports)
    return(count, part2_list) 

def part2():
    passports = part1()[1]
    c = 0
    for passport in passports:
        has_height = hgt.match(passport['hgt'])
        incm = re.sub('[0-9]', '', passport['hgt'])



        if 1920 <= int(passport['byr']) <= 2002:
            # passports.remove(passport)
            
            if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
                # passports.remove(passport)
                
                if 2020 <= int(passport['eyr']) <= 2030:
                    # passports.remove(passport)
                    c+=1
                    
        # if not has_height:
        #     passports.remove(passport)
        #     continue
        # elif incm == 'cm' and 150 <= int(passport['hgt'][:-2]) <=193 or\
        #     incm == 'in' and 59 <= int(passport['hgt'][:-2]) <=76:
        #     passports.remove(passport)
        #     continue
             



        # elif re.sub('[0-9]', '', passports['hgt']) == 'cm':
        #      if height < 150 and height > 193:
            #         return()
            # elif re.sub('[0-9]', '', passports['hgt']) == 'in':
            #     if height < 59 and height > 76:
            #         return()
            # else:
            #     return()
       
            # if not hcl.match(passports['hcl']):
            #     return()
            # if not ecl.match(passports['ecl']):
            #     return()
            # if not pid.match(passports['pid']):
            #     return()
        # else:
        #     c+=1    
    # return(len(passports)) 
    return(c)      
            
                
 



# print(part2())


print(part1(read_lines()[0]))
    

  

