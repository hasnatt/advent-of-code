numbers_list = [line.rstrip() for line in open('input.txt')]
z = 0
for i in numbers_list:
    
    command = i.split()
    positions = [int(i) for i in command[0].split('-')]
    letter = command[1].replace(':', '')
    password = command[2]
    count = password.count(letter)
    if(count >= positions[0] and count <= positions[1]):
        # print('valid')
        # print(f'password: {password}\t letter: {letter}\t count: {count}\t rule: {command[0]}')
        z+=1

print(f"Valid Passwords: {z}")
 