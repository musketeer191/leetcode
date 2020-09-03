def build_perms_from_index_perms(ls, index_perms):
    perms = []
    for p in index_perms:
        a_perm = []
        for p_i in p:
            a_perm.append(ls[p_i - 1])  # as python indexing start from 0
        perms.append(a_perm)

    return perms


def make_perms_of_int(n):
    # let perms[k] be the list of all permutations of 1:k, we will need perms[n]

    perms = []
    # init perms[k] as empty list, for each k in 1:n
    for k in range(n + 1):
        perms.append([])
    perms[1] = [[1]]
    for k in range(2, n + 1):
        # build perms[k] given perms[k-1]
        for p in perms[k - 1]:
            perm_start_with_k = [k] + p
            perms[k].append(perm_start_with_k)
            for i in range(2, k+1):
                a_perm_of_size_k = p[:i - 1] + [k] + p[i - 1:]
                perms[k].append(a_perm_of_size_k)
        # print('\tperms of indices from 1 to', k)
        # print('\t', perms[k])
    index_perms = perms[n]
    return index_perms


def make_perms(ls) -> list:
    # NOTE: suppose len(ls) = n, if we  can list all perms of its indices, ie. natural 1:n,
    #  then we can list all perms of the list. The perms of the indices can be built recursively.

    n = len(ls)
    index_perms = make_perms_of_int(n)
    return build_perms_from_index_perms(ls, index_perms)


if __name__ == '__main__':
    perms = make_perms([2, 4, 6, 8, 10])
    print('# perms:', len(perms))
    print('Perms:')
    print(perms)
