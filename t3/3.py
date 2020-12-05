with open("input.txt", "r") as fd:
    input_data = fd.readlines()
    input_data = [row.strip() for row in input_data]


TREE = "#"
SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def tree_count(r, d=1):
    num_of_trees = 0
    position = 0

    for idx in range(0, len(input_data), d):
        row = input_data[idx]
        if row[position] == TREE:
            num_of_trees += 1

        position += r

        if position >= len(row):
            position = position - len(row)

    return num_of_trees


result = 1
for x in [tree_count(r, d) for r, d in SLOPES]:
    result = result * x

print(tree_count(*SLOPES[1]))
print(result)
