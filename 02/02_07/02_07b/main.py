# Linear Search

# Aram workfile

my_list = [8, 0, 3, 6, 15, 7]

ITEM = 7

def search(item, listy):
    for elem in listy:
        if (item == ITEM):
            return True
    return False

print(search(ITEM, my_list))    

## use built-in python search function
ITEM_IDX = my_list.index(ITEM)
print(ITEM_IDX)