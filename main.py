cube = [
    (
        "A", "B", "C",
        "D", "E", "F",
        "G", "H", "I",
    ),
    (
        "J", "K", "L",
        "M", "N", "O",
        "P", "Q", "R",
    ),
    (
        "S", "T", "U",
        "V", "W", "X",
        "Y", "Z", "1",
    ),
    (
        "2", "3", "4",
        "5", "6", "7",
        "8", "9", "0",
    ),
    (
        "_", ".", ",",
        "?", "!", ")",
        "(", "}", "{",
    ),
    (
        ":", ";", "*",
        "-", "/", "&",
        "|", "~", "=",
    ),
]

def encode(input_str, cube):
    indexs = []

    for i in input_str:
        if i == "№":
            indexs.append(-1)
            continue
        else:
            for j in cube:
                if i in j:
                    n = cube.index(j) + 4
                    if n > 5:
                        n -= 6
                    hui = (n, j.index(i))
                    indexs.append(hui)
                else:
                    continue

    result = []

    for i in range(len(indexs)):
        if indexs[i] == -1:
            result.append("№")
            continue
        result.append(cube[indexs[i][0]][indexs[i][1]])

    print(''.join(map(str, result)))
    return ''.join(map(str, result))


def decode(input_str, cube):
    indexs = []

    for i in input_str:
        if i == "№":
            indexs.append(-5)
            continue
        else:
            for j in cube:
                if i in j:
                    n = cube.index(j) - 4
                    hui = (n, j.index(i))
                    indexs.append(hui)
                else:
                    continue

    result = []

    for i in range(len(indexs)):
        if indexs[i] == -5:
            result.append(" ")
            continue
        result.append(cube[indexs[i][0]][indexs[i][1]])

    print(''.join(map(str, result)))
    return ''.join(map(str, result))


# decode("!(&=", cube)
#
#
#
# input_str = input("Введите строку для дальнейших действий: ").replace(" ", "№").upper()
# choice = input("Какие ваши дальнейшие действия(encode, decode)?: ")
#
# if choice == "encode":
#     print(encode(input_str, cube))
# elif choice == "decode":
#     pass
# else:
#     print("Неправильной выбранное действие! Попробуйте еще раз!")

