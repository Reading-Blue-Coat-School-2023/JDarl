import random
plate = 'XX77 ABC'

def validate(num):
    valid = False
        
    while not valid:

        if len(num) == 8:
            if num[0].isalpha() and num[1].isalpha() and num[2].isdigit() and num[3].isdigit() and num[5].isalpha() and num[6].isalpha() and num[7].isalpha():
                valid = True
                return valid
            else:
                print('Incorrect pattern')
                num = input('Please enter the registaration: ')

        else:
            print('Enter a valid length numberplate')
    
def mph (speed):
    s_mph = speed *  2.237

    return(s_mph)

DISTANCE = 1609.34
SPEED_LIMIT = 70.0
GATE1 = 0

if validate(plate) is True:

    gate2 = float(input('Please input the time it took to reach gate 2 in seconds: '))   
    speed = DISTANCE / gate2
    milesph = mph(speed)
    
    print(milesph,'miles per hour')

if milesph > SPEED_LIMIT:
    f = open("speeding.txt", 'w')
    f.write(str(milesph))

def random_speed():
        time = random.randint(0,150)
        time = str(time)
        time += ' miles per hour'
        return time

def random_plate():
    plate = ''
 
    for i in range(2):
        plate += chr(random.randint(97,122))
 
    for j in range(2):
        plate += str(random.randint(0,9))
    plate += ' '    
    for k in range(3):
        plate += chr(random.randint(97,122))
    plate = plate.upper()
    return plate
    
print(random_plate())
print(random_speed())