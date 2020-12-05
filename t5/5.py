with open("input.txt", "r") as fd:
    input_data = fd.readlines()
    input_data = [row.strip() for row in input_data]

NUM_OF_ROWS = 128
NUM_OF_COLS = 8

FRONT = "F"
BACK = "B"
LEFT = "L"
RIGTH = "R"


def find_place(series, number_of_entries, upper_marker, lower_marker):
    lower_limit = 1
    upper_limit = number_of_entries

    for s in series:
        mid = ((lower_limit-1) + upper_limit) / 2

        if s == lower_marker:
            upper_limit = mid
        else:
            lower_limit = mid + 1
    else:
        return (upper_limit if s == upper_marker else lower_limit) - 1


def get_seat_id(ticket):
    row_markers = ticket[:-3]
    column_markers = ticket[-3:]

    row = find_place(row_markers, NUM_OF_ROWS, BACK, FRONT)
    col = find_place(column_markers, NUM_OF_COLS, RIGTH, LEFT)

    return (row * 8) + col


seat_ids = [get_seat_id(row) for row in input_data]
seat_ids.sort()

print(f"Max seat_id: {int(max(seat_ids))}")


for idx in range(len(seat_ids)):
    previous = seat_ids[idx-1]
    current = seat_ids[idx]
    if current - previous > 1:
        print(f"Free seat_id: {int(previous + 1)}")
