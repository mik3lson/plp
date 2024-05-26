#creating a function that detects palindrome

string = input("enter a word: ")
def is_palindrome(string):
    if string == string[::-1]:
        print (string, "is a palindrome")
    else:
        print (string, "is not a palindrome")

is_palindrome(string)