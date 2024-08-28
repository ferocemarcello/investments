import sys

# Read user input from command line arguments

deposited_value = float(sys.argv[1])
deposit_month = float(sys.argv[2])
number_years = int(sys.argv[3])
inter_month = float(sys.argv[4])
tax = float(sys.argv[5])

deposit_month_list = [deposit_month]*12*number_years
wallet_value = deposited_value
for i in range(len(deposit_month_list)):
    deposited_value+=deposit_month_list[i]

    monthly_gain = wallet_value * (inter_month-1)
    monthly_gain_taxed = (1-tax)*monthly_gain

    wallet_value *= inter_month
    wallet_value+=deposit_month_list[i]
    if (i+1)%12==0:
        print("after "+str((i+1)/12)+" years, wallet value: " + str(wallet_value) +"\ndeposited value: "+ str(deposited_value))
        print("ROI: " + str(wallet_value/deposited_value))
        print("Monthly gain, taxed: " + str(monthly_gain_taxed))
        print("")

print("value when withdrawed after taxes: "+str(deposited_value+(1-tax)*(wallet_value-deposited_value)))
