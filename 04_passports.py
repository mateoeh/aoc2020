import re
from typing import Callable

REQ_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open("inputs/4") as f:
    passports = f.read().strip().split("\n\n")


def is_valid(passport: str, entry_pred: Callable) -> bool:
    fields = set()
    for entry in re.split("[\n ]", passport):
        field, value = entry.split(":")
        fields.add(field)
        if not entry_pred(field, value):
            return False
    return set.issubset(REQ_FIELDS, fields)


# Problem 1
print(sum(1 for p in passports if is_valid(p, lambda f, v: True)))


def validator(field: str, value: str) -> bool:
    try:
        if field == "byr":
            return 1920 <= int(value) <= 2002
        elif field == "iyr":
            return 2010 <= int(value) <= 2020
        elif field == "eyr":
            return 2020 <= int(value) <= 2030
        elif field == "hgt":
            if value.endswith("cm"):
                return 150 <= int(value[:-2]) <= 193
            elif value.endswith("in"):
                return 59 <= int(value[:-2]) <= 76
            else:
                return False
        elif field == "hcl":
            return bool(re.match("^#[0-9a-f]{6}$", value))
        elif field == "ecl":
            return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        elif field == "pid":
            return bool(re.match("^[0-9]{9}$", value))
        elif field == "cid":
            return True
        else:
            return False
    except ValueError:
        return False


print(sum(1 for p in passports if is_valid(p, validator)))
