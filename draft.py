d = {'a': 1, 'b': 2}
sorted(d.items(), key=lambda x: x[1])


def find_last_occur(v, ls):
    # last occur is the first occur in reverse order
    try:
        return len(ls) - 1 - ls[::-1].index(v)
    except ValueError:
        return -1


if __name__ == '__main__':
    ls = [4, 5, 6, 4, 5]
    print(find_last_occur(4, ls))
