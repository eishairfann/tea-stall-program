# Tea Stall Program

# Read number of cups sold
N = int(input("Enter number of cups sold: "))

total_earnings = 0
special_count = 0

for i in range(1, N + 1):
    price = int(input(f"Enter price of cup {i}: "))

    if price < 40:
        print("Regular Tea")
    else:
        print("Special Tea")
        special_count += 1
    
    total_earnings += price

# Final output
print("Total Earnings:", total_earnings)
print("Special Teas Sold:", special_count)
