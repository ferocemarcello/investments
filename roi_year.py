import sys

# Read user input from command line arguments
initial_value = float(sys.argv[1])
deposit_year = float(sys.argv[2])
number_years = int(sys.argv[3])
inter_year = float(sys.argv[4])
tax = float(sys.argv[5])

deposit_year_list = [deposit_year]*number_years
wallet_value = initial_value
deposited_value = initial_value
count_years = 1
for deposit in deposit_year_list:
    wallet_value+=deposit
    deposited_value+=deposit
    wallet_value = wallet_value * inter_year
    print(f"after {count_years} years:\n\twallet value: {wallet_value}.\n\tdeposited value: {deposited_value}")
    print(f"\tROI: {(wallet_value/deposited_value)}\n")
    count_years +=1

taxed_value = tax*(wallet_value-deposited_value)
wallet_after_taxes = wallet_value-taxed_value
print(f"Wallet value when withdrawed after taxes: {wallet_after_taxes}")
