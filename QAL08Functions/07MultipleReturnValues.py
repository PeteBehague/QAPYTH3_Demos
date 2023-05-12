def calculate_data(sales):
    over_target = 0

    for s in sales:
        if s > 500: # 500 represents sales target
            over_target += 1

    average_sale = sum(sales) / len(sales)

    return over_target, average_sale

sales = (2000, 400, 800, 200)
o_t, a_s = calculate_data(sales)
print(f"Number over target: {o_t}, average sale: {a_s}")
