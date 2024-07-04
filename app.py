# Present the user with 4 selections:
# Add two numbers
# Subtract two numbers
# Multiply two numbers
# Divide two numbers
# Take user input for their choice
# the type and enter either 1, 2, 3 or 4
# Take user input for number one and number two.
# Apply the action based on the user choice to the given numbers
# Show the user the result
# Create a function that takes two arguments, adds them together and returns the result
# Create a function that takes two arguments, subtracts them and returns the result
# Create a function that takes two arguments, multiplies them and returns the result
# Create a function that takes two arguments, divides them and returns the result

def calculate(type):
    if user_input == 1:
        print("Please enter two numbers to add:")
        ans = inputs()
        return(ans[0] + ans[1])

    elif user_input == 2:
        print("Please enter two numbers to subtract:")
        ans = inputs()
        return(ans[0] - ans[1])

    elif user_input == 3:
        print("Please enter two numbers to multiply:")
        ans = inputs()
        return(ans[0] * ans[1])

    elif user_input == 4:
        print("Please enter two numbers to divide:")
        ans = inputs()
        return(ans[0] / ans[1])

def inputs():
    try:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
    except ValueError:
        print("Please enter a valid number.")
        num1 = 0
        num2 = 0
    
    return [num1, num2]

try:
    user_input = int(input("Please select one of the following options: \n 1. Add two numbers \n 2. Subtract two numbers \n 3. Multiply two numbers \n 4. Divide two numbers \nPlease enter a number: "))

except ValueError:
    user_input = 0
    print("Please enter a valid option.")

else: 
    print('Answer: ', calculate(user_input))

