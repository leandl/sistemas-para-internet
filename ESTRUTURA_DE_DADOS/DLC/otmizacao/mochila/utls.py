from entities.individual import Individual

def revert_compare(callback):
    return lambda i1, i2: callback(i1, i2) * -1

def compare_item(item1: "Individual", item2: "Individual") -> int:
    if item1.get_score() == item2.get_score():
        return 0
    
    return 1 if item1.get_score() > item2.get_score() else -1