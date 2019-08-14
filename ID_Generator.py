import random
import string


def get_letter():
    letter_string = []
    area_list = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34, 'J':18, 'K':19, 'M':21,
                 'N':22, 'O':35, 'P':23, 'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33}
    area_letter = random.choice(string.ascii_uppercase)
    while area_letter != None:
        if area_letter in area_list:
            break
        else: area_letter = random.choice(string.ascii_uppercase)
    area_num = str(area_list[area_letter])
    letter_string.append(area_letter)
    for index in range(len(area_num)):
        letter_string.append(area_num[index])
    "print('Letter_string is', letter_string)"
    return letter_string

def gender():
    gender = []
    gender.append(str(random.randint(1,2)))
    'print(gender, type(gender))'
    return gender

def random_seven_numbers():
    random_seven_numbers = []
    for times in range(7):
        number = str(random.randint(0,9))
        random_seven_numbers.append(number)
    'print(random_seven_numbers)'
    return random_seven_numbers

def check_number(source_list):
    check_number = []
    total = 0
    verify = [1,9,8,7,6,5,4,3,2,1]
    for index in range(len(source_list)):
        total += int(source_list[index]) * verify[index]
    "print(total)"
    if total % 10 == 0:
        check_number.append('0')
        "print('Rest num is 0')"
        return check_number
    else:
        check_number.append(str(10 - total % 10))
        "print('Rest num is ', total % 10, 'so return ', 10 - total % 10)"
        return check_number

def convert_to_normal_format(letter, ID_number_list):
    id_element = letter[0]
    for element in ID_number_list[2:]:
        id_element += element
    return id_element

if __name__ == '__main__':
    ID_number_list = []
    letter = get_letter()
    gender = gender()
    numbers = random_seven_numbers()
    ID_number_list = letter[1:3] + gender + numbers
    last_num = check_number(ID_number_list)
    ID_number_list += last_num
    final_id = convert_to_normal_format(letter, ID_number_list)
    print(final_id)
