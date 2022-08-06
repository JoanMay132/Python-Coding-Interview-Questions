'''
# You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) 
  and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.
'''
from art import logo
print(logo)
def two_sort(array):
    # your code here
    return "***".join(min(array))

input_string=input("Enter elements of a list separated by space: ")
user_list=input_string.split()
print(user_list)

print(two_sort(user_list))