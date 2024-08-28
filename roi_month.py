import sys

# Read user input from command line arguments
initial_value = float(sys.argv[1])
deposit_month = float(sys.argv[2])
number_years = float(sys.argv[3])
inter_month = float(sys.argv[4])
tax = float(sys.argv[5])

deposit_month_list = [deposit_month]*12*number_years

for i in range(len(deposit_month)):
    value+=deposit_month_list[i]
    initial_value+=deposit_month_list[i]
    monthly_gain = value * (inter_month-1)
    monthly_gain_taxed = (1-tax)*monthly_gain
    value = value * inter_month
    if (i+1)%12==0:
        print("after "+str((i+1)/12)+" years, wallet value: " + str(value) +"\ndeposited value: "+ str(initial_value))
        print("ROI: " + str(value/initial_value))
        print("Monthly gain, taxed: " + str(monthly_gain_taxed))
        print("")
    if (i+1)%12==0 and (i+1)/12 == 10:
        value+=1000000

print("value when withdrawed after taxes: "+str((1-tax)*(value-initial_value)))
