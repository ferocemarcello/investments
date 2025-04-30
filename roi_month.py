import sys

# Read user input from command line arguments
initial_value = float(sys.argv[1])
deposit_month = float(sys.argv[2])
number_years = int(sys.argv[3])
inter_month = float(sys.argv[4])
tax = float(sys.argv[5])

deposit_month_list = [deposit_month]*12*number_years
wallet_value = initial_value
deposited_value = initial_value
count_month = 1
for deposit_month in deposit_month_list:
    wallet_value+=deposit_month
    deposited_value+=deposit_month
    wallet_value = wallet_value * inter_month
    if count_month % 12 == 0:
        print(f"after {count_month/12} years:\n\twallet value: {wallet_value}.\n\tdeposited value: {deposited_value}")
        print(f"\tROI: {(wallet_value/deposited_value)}\n")
    count_month +=1

taxed_value = tax*(wallet_value-deposited_value)
wallet_after_taxes = wallet_value-taxed_value
print(f"Wallet value when withdrawed after taxes: {wallet_after_taxes}")
