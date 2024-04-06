# O(n) time | O(d) space
def flatten(array, depth=1):
    nums = []
    for i in range(0, len(array)):
        if type(array[i]) is list:
            if depth == 1:
                nums.extend(flatten(array[i], depth+1))
            else:
                nums.append(flatten(array[i], depth+1))
        else:
            nums.append(array[i])
    return nums
