# Writing a script that converts Kilometers to Miles
kilometers = float(input("Enter distance in kilomteres: "))

# Converting to miles (1 Km = 0.6213)
miles = kilometers * 0.6213

# Output the results
print(f"\n{kilometers} km = {miles} mi\n\n") # Adding the new line code to create an easier to read aesthetic for the user
print(f"Press any button to exit") # Adding this line of code because the results don't populate before the entire code closes out on itself
