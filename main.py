def define_array(SInputFile):  # заполнение массива числами из файла

    a = []

    with open(SInputFile) as f:
        while True:
            try:
                s = f.readline()  # считываем символ

                if not s:  # выходим, если конец
                    break

                s = s.split()

                for i in range(len(s)):
                    a.append(int(s[i]))

            except ValueError:
                print("Error: bad value.")
            except FileNotFoundError:
                print("Error: file not found.")

    return a


def print_array(array, l):

    for i in range(l):
        print(array[i])


def delete_rise_section(a):  # a - массив, l - длина этого массива

    i = 0

    while i < len(a):
        # print("len = ", len(a))
        # print("i = ", i)
        if i + 3 == len(a):  # провер.последн.эл-ты,чтобы избежать выхода за пределы массива
            if a[i - 1] >= a[i] and  a[i - 1] >= a[i] and a[i] < a[i + 1] < a[i + 2]:
                # print("Expect rise section:", a[i], a[i + 1], a[i + 2])
                for j in range((i + 2), i - 1, -1):
                    # print("j = ", j)
                    a.pop(j)
                # print(a)
                break

            if a[i - 1] >= a[i] and a[i] < a[i + 1] and a[i + 1] >= a[i + 2]:
                # print("Expect rise section:", a[i], a[i + 1])
                a.pop(i + 1)
                a.pop(i)
                # print(a)
                break

        elif i + 2 == len(a):  # проверка посл.эл-ов
            # print("len = ", len(a))
            # print("i = ", i)
            if a[i - 1] >= a[i] and a[i] < a[i + 1]:
                # print("Expect rise section:", a[i], a[i + 1])
                a.pop(i + 1)
                a.pop(i)
                # print(a)
            break

        elif i + 1 == len(a):
            break

        else:
            if a[i - 1] >= a[i] and a[i] < a[i + 1] < a[i + 2] and a[i + 2] >= a[i + 3]:
                # print("Expect rise section:", a[i], a[i + 1], a[i + 2])
                for j in range((i + 2), i - 1, -1):
                    a.pop(j)
                # print(a)
                continue

            if a[i - 1] >= a[i] and a[i] < a[i + 1] and a[i + 1] >= a[i + 2]:
                # print("Expect rise section:", a[i], a[i + 1])
                a.pop(i + 1)
                a.pop(i)
                # print(a)
                continue

        i += 1

    return len(a)


def main():

    print("-------------------")
    print("The original array:")
    arr = define_array("1.txt")
    print_array(arr, len(arr))
    print("-------------------")

    delete_rise_section(arr)

    print("--------------")
    print("Changed array:")
    print_array(arr, len(arr))
    print("--------------")

    return 0


main()
