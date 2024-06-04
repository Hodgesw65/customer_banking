# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter your savings account balance: "))
    savings_interest = float(input("Please enter the interest rate for the savings account (%): "))
    savings_maturity = int(input("Please enter the total number of months you intend to keep cash in your savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest earned on savings account: ${interest_earned:.2f}")
    print(f"Updated savings account balance with interest earned: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Please enter your CD account balance: "))
    cd_interest = float(input("Please enter the APR interest rate for the CD (%): "))
    cd_maturity = int(input("Enter the length of months the CD needs to be held until it matures: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest earned on CD account: ${interest_earned_cd:.2f}")
    print(f"Updated CD account balance with interest earned: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function..
    main()
