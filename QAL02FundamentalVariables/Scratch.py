import random

last_names = ["smith", "jones", "carpenter", "Patel"]

for lnname in last_names:
    ln_line_count = sum(1 for name in last_names)
    ln_line_number = random.randint(0, ln_line_count - 1)
    new_last_name = str(last_names[ln_line_number])
    print(new_last_name)