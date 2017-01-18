def find_missing(list1, list2):
    if type(list1) != list or type(list2) != list:
        return "Both parameters should be of type list"
    else:
        if len(list1) > len(list2):
            for el in list1:
                if el not in list2:
                    print(el)
                    return el
        if len(list1) < len(list2):
            for el in list2:
                if el not in list1:
                    print(el)
                    return el
        else:
            print(0)
            return 0

# find_missing([2,3,4], [2,3,4])
# find_missing([], [])
# find_missing([2], [2])
# find_missing([7], [7])
# find_missing([1, 2], [1, 2, 5])
# find_missing([4, 6, 8], [4, 6, 8, 10])
# find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])