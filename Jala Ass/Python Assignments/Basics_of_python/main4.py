n = "I am a global variable"

def fun():

    n = "I am a local variable"
    print("Inside function:", n)

fun()

print("Outside function:", n)
