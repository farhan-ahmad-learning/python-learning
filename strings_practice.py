# STRINGS DEEP PRACTICE
# Week 1 = Friday

# -----Block 1 - String Slicing-------------------------
name = "Farhan Ahmad"

print(name[0])      # F - first character
print(name[-1])     # d - last character
print(name[0:6])    # Farhan - characters 0 to 5
print(name[7:])     # Ahmad - from position 7 to end
print(name[:6])     # Farhan - start to 5
print(name[::2])    # every second character
print(name[::-1])   # reverse the string



# -----Block 2 - String useful methods -------------------------
sentence = "Python is Amazing for localization work"

print(sentence.strip())             # remove spaces
print(sentence.lower())             # all lower case
print(sentence.upper())             # all upper case
print(sentence.capitalize())        # first letter capitalised
print(sentence.title())             # first letter of each work capitalised
print(sentence.count("o"))          # count occurences of "o"
print(sentence.find("Amazing"))     # find position of word
print(sentence.replace("Amazing", "Perfect"))
print(sentence.strip().split(" "))  # split into list of words



# -----Block 3 - String checking methods -------------------------
test1= "12345"
test2 = "Farhan"
test3 = "farhan123"
test4 = "   "

print(test1.isdigit())      # True - all digits?
print(test2.isalpha())      # True - all letters?
print(test3.isalnum())      # True - letters and digits?
print(test4.isspace())      # True - all spaces?
print(test2.istitle())      # False - title case? (F is upper but rest lower = True actually)

# Very useful for validating user input!
age_input = input("Enter your age: ")
if age_input.isdigit():
    print(f"Valid age: {int(age_input)}")
else:
    print(f"Please enter a number only")



# -----Block 4 - String joining and splitting-------------------------
# Split - turn a string into a list
full_name = "Farhan ahmad Cognizant Delhi"
words = full_name.split(" ")
print(words)                    # ['Farhan', 'ahmad', 'Cognizant', 'Delhi']
print(words[0])                 # Farhan
print(words[-1])                # Delhi
print(len(words))               # 4 (no. of words)

#Join - turn a list back into a string
languages = ["Python", "French", "English", "Arabic"]
print(", ".join(languages))     # Python, French, English, Arabic
print(" | ".join(languages))    # Python | French | English | Arabic
print(" - ".join(languages))    # Python - French - English - Arabic
# Very useful in localization - joining translated segments!


