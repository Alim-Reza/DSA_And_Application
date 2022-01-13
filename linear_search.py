random_number_array = [0, 2, 5, 3, 6, 1]
search_key = int(input())

def linear_search(arr, key):
    for i in arr:
        if i == key:
            return True
        else:
            pass
    return False

print(linear_search(random_number_array, search_key))
