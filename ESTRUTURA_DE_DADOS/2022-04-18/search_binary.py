from utils import debug, timer

@debug
def searchBinary(listSearch, value):
    index_max = len(listSearch)
    index_min = 0

    while index_min <= index_max:
        index_mid = (index_min + index_max) // 2
        item = listSearch[index_mid]

        if item == value:
            return index_mid
        elif value > item:
            index_min = index_mid + 1
        else:
            index_max = index_mid - 1

    return None
   

searchBinary(list(range(100)), 6)
