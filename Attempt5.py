# Writing a script that converts Kilometers to Miles
kilometers = float(input("Enter distance in kilomteres: "))

# Converting to miles (1 Km = 0.6213)
miles = kilometers * 0.6213

# Output the results
print(f"\n{kilometers} km = {miles}:2f mi\n\n") # I did not want the decimal place of miles to be to the ten-thousandth place, so I condensed it to the hundredth place
print(f"Press the 'ENTER' button to exit") # Realized that any other key function on the keyboard does not end the function of the code until entering the information
input()
