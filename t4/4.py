import re


with open("input.txt", "r") as fd:
    input_data = fd.readlines()
    input_data = [row.strip().split(" ") for row in input_data]


REQUIRED_FIELD = [
    ("byr", (lambda x: True if 1920 <= int(x) <= 2002 else False)),
    ("iyr", (lambda x: True if 2010 <= int(x) <= 2020 else False)),
    ("eyr", (lambda x: True if 2020 <= int(x) <= 2030 else False)),
    ("hgt", (lambda x: validate_hgt(x))),
    ("hcl", (lambda x: validate_hcl(x))),
    ("ecl", (lambda x: validate_ecl(x))),
    ("pid", (lambda x: all(i.isdigit() for i in x) and len(x) == 9)),
]


def validate_hgt(heigth):
    measure = int(heigth[:-2])
    unit = heigth[-2:]
    if unit == "cm":
        return 150 <= measure <= 193
    else:
        return 59 <= measure <= 76


def validate_hcl(hcl):
    return re.findall("^#[0-9a-f]{6}$", hcl)


def validate_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


passports = []
passport = {}

for row in input_data:
    if row[0] == "":
        passports.append(passport)
        passport = {}
    else:
        for pair in row:
            key = pair[:3]
            value = pair[4:]
            passport[key] = value
else:
    passports.append(passport)


def invalid_1():
    invalid = 0
    for p in passports:
        for f in REQUIRED_FIELD:
            key, validtor = f
            if key not in p:
                invalid += 1
                break
    return invalid


def invalid_2():
    invalid = 0
    for p in passports:
        for f in REQUIRED_FIELD:
            key, validtor = f
            if key not in p:
                invalid += 1
                break
            else:
                if not validtor(p[key]):
                    invalid += 1
                    print(p[key], key)
                    break
    return invalid


print("1", len(passports) - invalid_1())
print("2", len(passports) - invalid_2())
