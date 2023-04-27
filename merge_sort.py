def merge_sorted_lists(a, b):
    new_list = []
    index_a = 0
    index_b = 0
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            new_list.append(a[index_a])
            index_a += 1
        else:
            new_list.append(b[index_b])
            index_b += 1
    if index_a == len(a):
        new_list.extend(b[index_b:])
    else:
        new_list.extend(a[index_a:])
    return new_list


def merge_sort(l):
    if len(l) > 1:
        middle = len(l) // 2
        list_a = merge_sort(l[:middle])
        list_b = merge_sort(l[middle:])
        return merge_sorted_lists(list_a, list_b)
    return l


l = [34, 56, 14, 20, 77, 51, 93, 30, 15, 52]
print(merge_sort(l))
