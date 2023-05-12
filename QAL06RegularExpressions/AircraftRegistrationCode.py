import re

valid_registration_marks = ["RA-12345", "B-1234", "B-123X", "B-12XX", "N12345", "G-ABCD"]
bad_registration_marks = ["N4561223", "N456F23", "D 456", "F-CDEF", "", "B 123A", "B-123456"]

all_registraion_marks = valid_registration_marks + bad_registration_marks

for reg_mark in all_registraion_marks:
    x = re.search(r"^RA-[0-9]{5}$|^G-[A-Z]{4}$|^N[0-9]{5}$|^B-[0-9]{2}[A-Z0-9]{2}$", reg_mark)
    if x:
        print(f"{reg_mark} is valid")
    else:
        print(f"{reg_mark} is invalid")
