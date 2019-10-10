

# Define a function like this
def a_function():
    print("Calling a function,")
    print("runs the code in the function.")

    a_result_variable = 3 * 5

    print("Our calculation result: " + str(a_result_variable) + "\n")


# call a function like this:
a_function()

# you can call it lots of times in a loop
for loop in range(0, 3):
    print("Loop " + str(loop) + ".")
    a_function()


# You can also pass actual variables, or arguments, into functions when you call them.
# First you need to define a function that takes input variables, or parameters
def another_function(input_variable_1, input_variable_2):
    print("Hey, another function!")
    print("1st variable: " + str(input_variable_1))
    print("2nd variable: " + str(input_variable_2))

    another_result_variable = input_variable_1 + input_variable_2

    # return lets us get data out of the function that can be assigned to variables
    return another_result_variable


# You can call our function by passing variables into it like this:
result = another_function(2, 10)
print("Our calculation result: " + str(result) + "\n")

# Or like this...
var_1 = result
var_2 = 6
another_result = another_function(var_1, var_2)
