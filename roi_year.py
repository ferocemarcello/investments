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
    print(f"after {count_years} years, wallet value: {wallet_value}.\ndeposited value: {deposited_value}")
    print(f"ROI: {(wallet_value/deposited_value)}")
    yearly_gain_taxed = (1-tax)*wallet_value
    print(f"Yearly gain, taxed: {yearly_gain_taxed}\n")
    count_years +=1

taxed_value = (1-tax)*wallet_value
print("Wallet value when withdrawed after taxes: "+str(taxed_value))
