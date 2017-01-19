class BinarySearch(list):
    def __init__(self, a, b):

        self.step = b
        self.a = a
        self.gen_list = [b for b in range(b, (a + 1) * b, b)]

    def search(self, value):
        result = {}
        count = 0
        # index = 0
        found = False
        first = 0
        last = len(self.gen_list) - 1
        if value == self.gen_list[last]:
            result['count'] = count
            result['index'] = last
            return result
        while first < last and not found:
            mid = (first + last) // 2

            if self.gen_list[mid] == value:
                found = True
                result['count'] = count
                result['index'] = mid
                print(result)
                return result
            else:
                if value < self.gen_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            count += 1
        result['count'] = count - 1
        if value in self.gen_list:
            result['index'] = mid+1
        else:
            result['index'] = -1
        print(result)
        # print(self.length)
        return result

BinarySearch(20, 2).search(33)