def get_mtch_seq(s, s2):
    res = []
    for s1 in s:
        j = 0
        add_s1 = True

        for i in range(len(s2)):
            flag = False
            while j < len(s1):
                if s1[j] == s2[i]:
                    j += 1
                    flag = True
                    break
                else:
                    j += 1
            if not flag:
                add_s1 = False
                break
        if add_s1:
            res.append(s1)
    return res


def rev(S):
    res = []
    for x in S:
        res = [x] + res
    return res


def get_mtch_seqREV(s, s2):
    s2 = rev(s2)
    res = []
    for s1 in s:
        j = 0
        add_s1 = True
        for i in range(len(s2)):
            flag = False
            while j < len(s1):
                if s1[j] == s2[i]:
                    j += 1
                    flag = True
                    break
                else:
                    j += 1
            if not flag:
                add_s1 = False
                break
        if add_s1:
            res.append(s1)
    return res


print(get_mtch_seq([], ["a"]))
print(get_mtch_seq([["", "a"], [], ["", "b"]], ["a"]))
print(get_mtch_seq([["a", "b", "c"], [], ["", "a"]], ["a", "c"]))
print(get_mtch_seqREV([], ["a"]))
print(get_mtch_seqREV([["a", "b", "c", "d"], [], ["a", "b"]], ["d", "b"]))
