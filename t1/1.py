def process(report):
    for idx, value1 in enumerate(report):
        canditate = 2020 - value1

        for value2 in report[idx+1: ]:
            if canditate == value2:
                return value1*value2


def process_three_numbers(report):
    for idx, value1 in enumerate(report):
        for idx2, value2 in enumerate(report[idx+1: ]):
            canditate = 2020 - value1 - value2

            for value3 in report[idx2: ]:
                if canditate == value3:
                    return value1*value2*value3


with open("input.txt", "r") as fd:
    input_data = fd.readlines()
    expense_report = [int(row.strip()) for row in input_data]
    print(process(expense_report))
    print(process_three_numbers(expense_report))

    #print([x for x in expense_report if 2020 - x in expense_report])
