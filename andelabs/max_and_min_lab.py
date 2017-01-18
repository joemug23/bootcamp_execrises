def find_max_min(arg):
    result = []
    if type(arg) != list:
        return "Input should be of list type"
    else:
        if min(arg) == max(arg):
            result.append(len(arg))
            return result

        result.append(min(arg))
        result.append(max(arg))
        return result
    