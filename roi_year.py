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
    print("after "+str(count_years)+" years, wallet value: " + str(wallet_value) +"\ndeposited value: "+ str(deposited_value))
    print("ROI: " + str(wallet_value/deposited_value))
    yearly_gain_taxed = (1-tax)*wallet_value
    print("Monthly gain, taxed: " + str
    (yearly_gain_taxed))
    print("")
    count_years +=1

taxed_value = (1-tax)*wallet_value
print("Wallet value when withdrawed after taxes: "+str(taxed_value))
