# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def true_even(input):
   if input % 2 == 0:
    print('True')
        

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
true_even(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def returns_even(input):
    if input % 2 == 0:
       print('Even!')
    else:
        print('Odd!')

returns_even(num)