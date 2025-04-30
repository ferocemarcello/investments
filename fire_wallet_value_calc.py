import sys

# Read user input from command line arguments
inter_month = float(sys.argv[1])
month_earn = float(sys.argv[2])
tax = float(sys.argv[3])

sell_month = month_earn/(1-tax)
print(f"sell_month: {sell_month}")
wv= sell_month/(inter_month-1)

print("wallet value to earn exactly what you sell per month: "+str(wv))
