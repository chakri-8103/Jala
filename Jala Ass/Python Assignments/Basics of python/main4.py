my_var = "I am a global variable"

def my_function():

    my_var = "I am a local variable"
    print("Inside function:", my_var)

my_function()

print("Outside function:", my_var)
