import sys

# Read user input from command line arguments
value = float(sys.argv[1])
deposit_year = float(sys.argv[2])
number_years = float(sys.argv[3])
inter_year = float(sys.argv[4])
tax = float(sys.argv[5])

for i in range(len(deposit_year)):
    value+=deposit_year[i]
    init_value+=deposit_year[i]
    value = value * inter_year
    print("after "+str(i+1)+" years, wallet value: " + str(value) +"\ndeposited value: "+ str(init_value))
    print("ROI: " + str(value/init_value))
    yearly_gain_taxed = (1-tax)*value
    print("Monthly gain, taxed: " + str
    (yearly_gain_taxed))
    print("")

tax=0.33
taxed_value = (1-tax)*value
print("value when withdrawed after taxes: "+str(taxed_value))
