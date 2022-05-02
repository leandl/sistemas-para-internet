from utils import debug, timer

@debug
def searchBinary(listSearch, num):
    number_item_max = len(listSearch)
    number_item_min = 0

    while number_item_min <= number_item_max:
        index = (number_item_min + number_item_max) // 2
        n2 = listSearch[index]
        print([n2, num])
        if n2 == num:
            return index
        elif n2 < num:
            number_item_min = index + 1
        else:
            number_item_max = index - 1

    return None

searchBinary([1, 3, 6, 10], 6)