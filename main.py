def define_array(SInputFile):  # заполнение массива числами из файла

    a = []
    ise = 0

    try:
        with open(SInputFile) as f:
            while True:
                s = f.readline()  # считываем символ

                if not s:  # выходим, если конец
                    break

                s = s.split()

                for i in range(len(s)):
                    a.append(int(s[i]))
                    ise += 1

    except ValueError:
        print("Error: bad value.")
        f.close()

        return -1
    except FileNotFoundError:
        print("Error: file not found.")

        return -1

    if ise == 0:
        print("Error: file is empty.")

        return -1

    return a


def print_array(array, l):

    for i in range(l):
        print(array[i])


def delete_rise_section(a):  # a - массив, l - длина этого массива

    i = 0
    canpop = 0

    while i < len(a):

        # print()
        # print("len = ", len(a))
        # print("i = ", i)
        # print("a[i] = ", a[i])
        #
        ifpop = len(a)
        # print("ifpop = ", ifpop)

        if i + 3 == len(a):  # провер.последн.эл-ты,чтобы избежать выхода за пределы массива
            # print("52")
            if (a[i - 1] >= a[i] or canpop > 0) and a[i] < a[i + 1] < a[i + 2]:
                # print("Expect rise section:", a[i], a[i + 1], a[i + 2])
                for j in range((i + 2), i - 1, -1):
                    # print("j = ", j)
                    a.pop(j)

                canpop += 1

                # print(a)
                break

            if (a[i - 1] >= a[i] or i == 0 or canpop > 0) and a[i] < a[i + 1] and a[i + 1] >= a[i + 2]:
                # print("Expect rise section:", a[i], a[i + 1])
                a.pop(i + 1)
                a.pop(i)

                canpop += 1

                # print(a)
                break

        elif i + 2 == len(a):  # проверка посл.эл-ов
            # print("len = ", len(a))
            # print("i = ", i)
            if (a[i - 1] >= a[i] or canpop > 0) and a[i] < a[i + 1]:
                # print("Expect rise section:", a[i], a[i + 1])
                a.pop(i + 1)
                a.pop(i)

                canpop += 1

                # print(a)
            break

        elif i + 1 == len(a):
            break

        else:
            # print("82")
            if (a[i - 1] >= a[i] or i == 0 or canpop > 0) and a[i] < a[i + 1] < a[i + 2] and a[i + 2] >= a[i + 3]:
                # print("Expect rise section:", a[i], a[i + 1], a[i + 2])
                for j in range((i + 2), i - 1, -1):
                    a.pop(j)

                canpop += 1

                # print(a)
                continue

            if (a[i - 1] >= a[i] or i == 0 or canpop > 0) and a[i] < a[i + 1] and a[i + 1] >= a[i + 2]:
                # print("Expect rise section:", a[i], a[i + 1])
                a.pop(i + 1)
                a.pop(i)

                canpop += 1

                # print(a)
                continue

        i += 1
        canpop = 0

    return len(a)


def main():

    arr = define_array("1.txt")

    if not isinstance(arr, int):
        print("-------------------")
        print("The original array:")
        print_array(arr, len(arr))
        print("-------------------")

        delete_rise_section(arr)

        print("--------------")
        print("Changed array:")
        print_array(arr, len(arr))
        print("--------------")

    return 0


main()
