# Найти индекс первого нуля
def task(array):
    left = -1
    right = len(array)
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] == '1':
            left = middle
        else:
            right = middle
    return right


print(task('111111111110000000000000000'))
