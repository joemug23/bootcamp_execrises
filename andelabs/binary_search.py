class BinarySearch(list):
    def __init__(self, a, b):

        self.step = b
        self.gen_list = [b for b in range(b, (a + 1) * b, b)]
        self.length = len(self.gen_list)

    def search(self, value):
        result = {}
        count = 5
        # index = 0
        found = False
        first = 0
        last = self.length - 1
        while first < last and not found:
            mid = (first + last) // 2
            count += 1
            if self.gen_list[mid] == value:
                found = True
                result['count'] = count
                result['index'] = mid
                print(result)
                return result
            else:
                if value < self.gen_list[mid]:
                    last = self.gen_list[mid] - 1
                else:
                    first = self.gen_list[mid] + 1
        result['count'] = count
        result['index'] = mid
        print(result)
        # print(self.length)
        return result

BinarySearch(20, 1).search(16)