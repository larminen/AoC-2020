with open("input.txt", "r") as fd:
    input_data = fd.readlines()
    input_data = [row.strip().split(" ") for row in input_data]


def parse_row(row):
    small_num, big_num = [int(pos) for pos in row[0].split("-")]
    required = row[1].strip(":")
    password = row[2]
    return small_num, big_num, password, required


def policy_1(input_data):
    incorrect_passwords = 0
    for row in input_data:
        min_count, max_count, password, required = parse_row(row)
        n = password.count(required)
        if min_count <= n <= max_count:
            incorrect_passwords += 1

    return incorrect_passwords


def policy_2(input_data):
    incorrect_passwords = 0
    for row in input_data:
        matches = 0
        pos1, pos2, password, required = parse_row(row)
        for pos in [pos1, pos2]:
            if password[pos-1] == required:
                matches += 1

        if matches == 1:
            incorrect_passwords += 1

    return incorrect_passwords


print(policy_1(input_data))
print(policy_2(input_data))
