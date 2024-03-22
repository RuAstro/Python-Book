def invest(amount, rate, years):
    """Display year on year growth of an initial investment"""
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:,.2f} ")

amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an return rate: "))
years = int(input("Enter number of years: "))

invest(amount, rate, years)
