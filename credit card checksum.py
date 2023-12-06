card_number = '4716784337571224'

valid = False

while not valid:

    if len(card_number) == 16:
        try: 
            int(card_number)
            valid = True
        except:
            print('Please enter an integer')
    else:
        print('Please enter a 16 digit number')

def checksum(card_no):
    total = 0
    
    for i in range(0, 16):
        digit = int(card_no[i])
        if i % 2 == 0:
            digit *= 2
            if digit >= 10:
                digit = digit // 10 + digit % 10
        total += digit

    if total % 10 == 0:
        return True
    else:
        return False
    
print(checksum(card_number))