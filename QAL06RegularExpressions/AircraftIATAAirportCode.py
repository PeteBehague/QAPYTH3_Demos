import re

valid_iata_codes = ["123", "12A", "1AB", "ABC", "AB1", "A12"]
bad_iata_codes = ["000", "1234", "123A", "A123", "", "ABCD", "12", "AB", "1A", "A1"]

all_iata_codes = valid_iata_codes + bad_iata_codes

for iata_code in all_iata_codes:
    x = re.search(r"^(?!0{3})[A-Z0-9]{3}$", iata_code)
    if x:
        print(f"{iata_code} is valid")
    else:
        print(f"{iata_code} is invalid")
