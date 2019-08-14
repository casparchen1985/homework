import random
import string

area_eng = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34, 'J':18, 'K':19, 'M':21,
            'N':22, 'O':35, 'P':23, 'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33}
verify = [1,9,8,7,6,5,4,3,2,1,1]
id_num_list = []
id_sum = 0
area_num = 0


while True:
    id_num_list.clear()
    input_str = input('Please input an ID: ')
    input_str = input_str.upper()

    if len(input_str) == 10:
        if input_str[0] in area_eng:
            if input_str[1] == '1' or input_str[1] == '2':
                if isinstance(int(input_str[3:len(input_str)]), int) == True:
                    area_num_str = str(area_eng[input_str[0]])
                    for index in range(len(area_num_str)):
                        id_num_list.append(area_num_str[index])

                    id_num_list.append(input_str[1])

                    for index in range(2, len(input_str)):
                        id_num_list.append(input_str[index])

                    for index in range(len(id_num_list)):
                        id_sum += int(id_num_list[index]) * verify[index]
                        "print(id_num_list[index])"
                    if id_sum%10 == 0:
                        print(input_str +' is a valid ID.')
                    else:
                        print('This is not an valid ID. verification is failed')
                        break
                else:
                    print('This is not an valid ID. Format is worng')
                    break
            else:
                print('This is not an valid ID. Gender is not match')
                break
        else:
            print('This is not an valid ID. Start with non-alphabet on correct alphabet')
            break
    else:
        print('This is not an valid ID. Lenth is not 10 digits')
        break