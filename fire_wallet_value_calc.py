import sys

# Read user input from command line arguments
inter_month = float(sys.argv[1])
sell_month = float(sys.argv[2])
tax = float(sys.argv[3])

wv = (sell_month*(1-tax))/(inter_month-1)
print("wallet value to earn exactly what you sell per month: "+str(wv))
