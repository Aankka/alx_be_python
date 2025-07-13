# This script asks the user for their current age and calculates
# how old they will be in the year 2050, assuming the current year is 2023.

# Prompt the user to input their current age
# The input() function reads a line from input, and int() converts it to an integer.
current_age = int(input("How old are you? "))

# Calculate how old the user will be in the year 2050.
# Assuming current year is 2023, the difference to 2050 is 27 years.
years_to_add = 2050 - 2023
future_age = current_age + years_to_add

# Print the user's age in 2050 in the specified format
print(f"In 2050, you will be {future_age} years old.")
