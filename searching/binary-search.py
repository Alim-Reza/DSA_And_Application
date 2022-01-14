random_number_array = [0, 1, 2, 3, 5, 6, 7]
search_key = 4

def binary_search(arr, key):
    startPoint = 0;
    endPoint = len(arr)
    while(True):
        midPoint = int((startPoint + endPoint) / 2)
        print(midPoint)
        if arr[midPoint] == key:
            return True
        elif startPoint == endPoint:
            return False
        else:
            if key > arr[midPoint]:
                startPoint = midPoint + 1
            else:
                endPoint = midPoint - 1

print(binary_search(random_number_array, search_key))
