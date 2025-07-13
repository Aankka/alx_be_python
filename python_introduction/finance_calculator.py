# This script calculates a user's monthly savings and projects
# potential future savings over a year with a simple interest rate.

# --- User Input for Financial Details ---
# Prompt the user to enter their monthly income.
# The input() function reads a string, and float() converts it to a floating-point number.
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses.
monthly_expenses = float(input("Enter your total monthly expenses: "))

# --- Calculate Monthly Savings ---
# Monthly savings are calculated by subtracting expenses from income.
monthly_savings = monthly_income - monthly_expenses

# --- Project Annual Savings ---
# Define the simple annual interest rate as a decimal.
annual_interest_rate = 0.05  # 5% annual interest rate

# Calculate the projected savings after one year.
# This includes the total savings over 12 months plus the interest earned on that amount.
# Formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_annual_savings = (monthly_savings * 12) + \
    (monthly_savings * 12 * annual_interest_rate)

# --- Output Results ---
# Display the user's calculated monthly savings.
# .2f for two decimal places
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Display the projected annual savings after including interest.
print(
    f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
