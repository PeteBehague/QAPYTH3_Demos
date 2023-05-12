import re


def validate_the_hard_way(value):
    if len(value) < 5 or len(value) > 7:
        return "Illegal Registration number, should be between 5 and 6 characters long"
    last_four_chars = value[-4:]
    first_char = value[:1]
    second_char = value[1:2]
    # Ensure last 3 characters are digits
    for ch in last_four_chars:
        if not ch in "1234567890":
            return "Illegal Registration Number, last 4 characters must be digits";
    # Ensure first characters are alpha
    if not first_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "Illegal Registration Number, first character must be alpha";
    # Ensure second character is space or digit
    if not second_char in " 1234567890":
        return "Illegal Registration Number, second character must be space or digit";
    return ""


def validate_the_regex_way(value):
    x = re.search(r"^[A-Z][\s]?[0-9]{4,5}$", value)
    return x


valid_boat_codes = ["A 0000", "P3333", "B11111", "Y 11111"]
bad_boat_codes = ["D456", "D 456", "BC123", "", "B 123A", "B 123456"]

all_boat_codes = valid_boat_codes + bad_boat_codes

print("HARD WAY")
for boat_code in all_boat_codes:
    x = validate_the_hard_way(boat_code)
    if not x:
        print(f"{boat_code} is valid")
    else:
        print(f"{boat_code} is invalid, message is {x}")

print("\nREGEX WAY")
for boat_code in all_boat_codes:
    x = not validate_the_regex_way(boat_code)
    if not x:
        print(f"{boat_code} is valid")
    else:
        print(f"{boat_code} is invalid")
