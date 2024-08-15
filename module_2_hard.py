number = (int(input('Введите число с первого поля, я подберу вам пароль: ')))


def find_password():
    password = []
    first_field = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for x in range(1, 21):
        for y in range(1, 21):
            if number % (x + y) == 0 and x != y:
                password.append([x, y])
            else:
                continue
    for couple1 in password:
        for couple2 in password:
            if couple1 == couple2:
                continue
            elif couple1[0] == couple2[1] and sum(couple2) == sum(couple1):
                password.remove(couple2)
            else:
                continue
    beautiful_password = ''
    for i in password:
        i = (''.join(map(str, i)))
        beautiful_password += i
    print(beautiful_password)


find_password()
