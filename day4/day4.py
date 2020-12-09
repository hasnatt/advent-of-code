KEYS = ['ecl', 'pid', 'eyr', 'hcl', 'byr','iyr', 'hgt']
lines = open("input.txt").read().split("\n\n")

count = 0 
for i in range(0,len(lines)):
    passport = lines[i].replace('\n', ' ').split()
    passport = [fields.split(':')[0] for fields in passport]
    if 'cid' in passport:
        passport.remove('cid')
    if set(KEYS) == set(passport):
        count+=1
    print(passport)
    
print(f"Part 1 Answer: {count}")    


