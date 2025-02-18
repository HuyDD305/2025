if __name__ == "__main__":
    x = int(input("Give me your x: "))
    y = int(input("Give me your y: "))
    z = int(input("Give me your z: "))
    n = int(input("Give me your total: "))
    testList = []

    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if i + j + k != n:
                    testList.append([i, j, k])

    print(testList)


