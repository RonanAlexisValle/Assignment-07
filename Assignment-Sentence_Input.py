# This program will count the words, vowels, and consonants of a sentence inputted by the user.
# After that the result will be displayed on the output console
# This program will use 'for' loops

# STEP-1: This will ask the user to input random sentence.

askUser = input("Input the sentence you want to analyze: ")

# STEP-2: The inputted sentence will go to this conditions.

count_Words = 1
count_Vowels = 0 
count_Consonants = 0

for x in askUser:
    if (x == " "):
        count_Words = count_Words + 1
    
    elif (x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U' or
        x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' ):
        count_Vowels = count_Vowels + 1

    else:
        count_Consonants = count_Consonants + 1

# STEP-3: The result will be displayed on the screen console.
print("The total number of words in the sentence are ", count_Words)
print("The total number of vowels in the sentence are ", count_Vowels)
print("The total number of consonants in the sentence are ", count_Consonants)

