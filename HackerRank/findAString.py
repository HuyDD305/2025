def count_substring(string, sub_string):
    count = 0

    alist = list(string)
    for i in range(0, len(alist)):
        number = 0
        aWord = ""
        while number < len(sub_string):
            if i > len(alist) - 1:
                break
            else:
                aWord = aWord + alist[i]
                i += 1
                number += 1
        print(f"What i want {sub_string}")
        print(f"What i calculate {aWord}")
        if aWord == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    testString = "ABCDCDC"
    testSub = "CDC"
    print(count_substring(testString, testSub))
