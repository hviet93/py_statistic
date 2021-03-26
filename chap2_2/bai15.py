import numpy as np


def main():
    data = [
        11.3, 9.6, 10.4, 7.5, 8.3, 10.5, 10.0,
        9.3, 8.1, 7.7, 7.5, 8.4, 6.3, 8.8
    ]
    stem_leaf_data = {}
    stem_data = []

    for val in data:
        if int(val) not in stem_data:
            stem_data.append(int(val))

    stem_data = np.sort(stem_data)[::1]

    for val in stem_data:
        stem_leaf_data[str(val)] = []

    for val in data:
        if str(int(val)) in stem_leaf_data:
            min_stem = int(val)
            max_stem = int(val) + 0.9

            if min_stem <= val <= max_stem:
                leaf_value = int(round(val - min_stem, 1) * 10)
                stem_leaf_data[str(min_stem)].append(leaf_value)

    for stem_leaf in stem_leaf_data:
        stem_leaf_str = " " + str(stem_leaf) + " | " \
            if int(stem_leaf) < 10 else str(stem_leaf) + " | "
        stem_leaf_data[str(stem_leaf)] = np.sort(stem_leaf_data[str(stem_leaf)])[::1]

        for leaf_val in stem_leaf_data[stem_leaf]:
            stem_leaf_str = stem_leaf_str + str(leaf_val) + " "

        print(stem_leaf_str)


main()
