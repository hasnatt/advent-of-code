numbers_list = [line.rstrip() for line in open('input.txt')]
z = 0
for i in numbers_list:
    
    command = i.split()
    positions = [int(i) for i in command[0].split('-')]
    letter = command[1].replace(':', '')
    password = command[2]
    count = password.count(letter)


    if(password[positions[0]-1] == letter and password[positions[1]-1] != letter):
        z+=1
    elif(password[positions[0]-1] != letter and password[positions[1]-1] == letter): 
        z+=1

print(f"Valid Passwords: {z}")