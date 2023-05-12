import re

valid_icao_codes = ["A123", "AB12", "ABC1", "ABCD", "A1BC", "A11B", "A1B1", "A12", "AB1", "ABC", "A1B", "A1", "AB"]
bad_icao_codes = ["000", "1234", "123A", "", "1BCD", "12", "1A", "A1234", "AB123"]

all_icao_codes = valid_icao_codes + bad_icao_codes

for icao_code in all_icao_codes:
    x = re.search(r"^[A-Z][A-Z0-9]{1,3}$", icao_code)
    if x:
        print(f"{icao_code} is valid")
    else:
        print(f"{icao_code} is invalid")