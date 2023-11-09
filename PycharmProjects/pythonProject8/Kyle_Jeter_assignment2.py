# Second Function for Calculation of Chocolate Count and Printing
def chocolatecalculation(money, coupon_count, choco):
    chocolate_per_coupon = 7
    # While statement for adding to chocolate count based on coupons
    while coupon_count >= 7:
        coupon_count -= 7
        choco += 1
        coupon_count += 1
        # Output statement to user
    print(f"You can buy {choco} chocolates\nYou will have {coupon_count} leftover coupons")


# Main Function Definition
def main():
    program_run = 'y'
    # While statement for looping program
    while program_run.lower() == 'y':
        # Variable initialization
        chocolates = 0
        coupons = 0
        coupons = choco_count = money_for_chocolates = int(input("How much would you like to spend on chocolates? "))
        while coupons < 0:
            coupons = choco_count = money_for_chocolates = int(input("Error: Please Enter a Positive Integer\n"
                                                                     "How much would you like to spend on chocolates? "))
        chocolatecalculation(money_for_chocolates, coupons, choco_count)  # Function call
        # Asking user if the program should continue looping
        program_run = input("Would you like to use this program again? (y/n) ")


main()




