import numpy as np


def main():
    data = [
        1161, 1206, 1478, 1300, 1604, 1725, 1361, 1422,
        1221, 1378, 1623, 1426, 1557, 1730, 1706, 1689
    ]
    stem_leaf_data = {}

    for val in data:
        stem_val = int(val / 100)
        leaf_val = int(val / 10) - stem_val * 10

        if str(stem_val) not in stem_leaf_data:
            stem_leaf_data[str(stem_val)] = [leaf_val]
        else:
            stem_leaf_data[str(stem_val)].append(leaf_val)

    stem_leaf_data = stem_leaf_data.items()
    stem_leaf_data = sorted(stem_leaf_data)

    for stem_leaf in stem_leaf_data:
        print(stem_leaf[0])
        print(type(stem_leaf[1]))

    # for stem_leaf in stem_leaf_data:
    #     stem_leaf_str = str(stem_leaf) + " | "
    #     stem_leaf_data[stem_leaf] = np.sort(stem_leaf_data[stem_leaf])[::1]
    #
    #     for leaf_val in stem_leaf_data[stem_leaf]:
    #         stem_leaf_str = stem_leaf_str + str(leaf_val) + " "
    #
    #     print(stem_leaf_str)


main()
