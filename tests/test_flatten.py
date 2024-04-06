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

def test_flatten():
    expected = [
        [1,2,3,7,8,9,5,6,4],
        [1, 2, 7, 4, 5, 2,[3, 8, 1], 9, 10],
        [0, 1, 2, [3, [4, 5], [6, 7, [8, 9]]]]
    ]
    flattened = [
        flatten([[1,2,3],[7,8,9],[5,6,4]]),
        flatten([1,2,[7,4],5,[2,[3,8,1],9],10]),
        flatten([0, 1, [2, [3, [4, 5], [6, 7, [8, 9]]]]])
    ]
    for i in range(0, len(flattened)):
        print(flattened[i])
        assert expected[i] == flattened[i]
