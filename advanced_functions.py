

# classes can also have functions!
# What the heck is a class? It is a way of grouping functions and data into useful concepts that help organise code
# we define a class like this
class HeyThisIsTheNameOfMyClass:

    # This is a special 'default' function of our class.
    # It is automatically called when you create an instance of a class
    def __init__(self):
        self.this_is_a_class_variable = "classy"  # we can access class variables in all the functions of our class

    # this is how we define a function in a class
    # note the indent to make it part of the class
    # and the self variable being passed in.
    # All class functions automatically pass in this
    # variable first so it has to be there
    def this_is_a_function_in_my_class(self, hey_a_variable):
        print("Check out me calling a class function")
        print("Hey it's a passed in variable: " + str(hey_a_variable))
        print("And here's a class variable: " + str(self.this_is_a_class_variable))


variable_to_pass_in = "passed in string"

# To call a class function we first need to create an object of the class.
# An object is also called an instance.
# This is how we do it. It's very similar to calling a function.
my_class_object = HeyThisIsTheNameOfMyClass()

# then we can call functions on the class using a . (a full stop) to join the name of the
# instance to the function name. Like so:
my_class_object.this_is_a_function_in_my_class(variable_to_pass_in)
