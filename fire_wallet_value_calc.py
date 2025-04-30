import sys

# Read user input from command line arguments
inter_month = float(sys.argv[1])
monthly_withdrawal = float(sys.argv[2])
tax = float(sys.argv[3])

sell_month = monthly_withdrawal/(1-tax)
print(f"sell_month: {sell_month}")
wv= sell_month/(inter_month-1)

print("wallet value to earn exactly what you sell per month: "+str(wv))
