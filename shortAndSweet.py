# simple solution
wordOne = input("Input first word to be compared: ")
wordTwo = input("Input second word to be compared: ")

if len(wordOne) > len(wordTwo):
    print("Shortest word is: " + wordTwo)
elif len(wordTwo) > len(wordOne):
    print("Shortest word is: " + wordOne)
elif len(wordOne) == len(wordTwo):
    print("They are the same size!")
else:
    print("Uh oh, something went wrong :(")

# optimised solution, includes string formatting and same length case is already handled
wordOne = input("Input first word to be compared: ")
wordTwo = input("Input second word to be compared: ")

if len(wordOne) > len(wordTwo):
    print(f"The shortest word is: {wordTwo}")
elif len(wordTwo) > len(wordOne):
    print(f"The shortest word is: {wordOne}")
else:
    print("Both words are of equal length.")

# using a function
def shortestWord(wordOne, wordTwo):
    if len(wordOne) > len(wordTwo):
        return wordTwo
    elif len(wordTwo) > len(wordOne):
        return wordOne
    else:
        return "Both words are of equal length."

wordOne = input("Input first word to be compared: ")
wordTwo = input("Input second word to be compared: ")

result = shortestWord(wordOne, wordTwo)
print(f"The shortest word is: {result}")