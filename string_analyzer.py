<<<<<<< HEAD
sentence = input("Enter a sentence: ")
words = sentence.split(" ")

print(f"Original            : {sentence}")
print(f"UPPERCASE           : {sentence.upper()}")
print(f"TitleCASE           : {sentence.title()}")
print(f"Reversed            : {sentence[::-1]}")
print(f"Total characters    : {len(sentence)}")
print(f"Without spaces      : {len(sentence.replace(" ",""))}")
print(f"Total words         : {len(words)}")
print(f"Starts with cap     : {sentence.istitle()}")
=======
sentence = input("Enter a sentence: ")
words = sentence.split(" ")

print(f"Original            : {sentence}")
print(f"UPPERCASE           : {sentence.upper()}")
print(f"TitleCASE           : {sentence.title()}")
print(f"Reversed            : {sentence[::-1]}")
print(f"Total characters    : {len(sentence)}")
print(f"Without spaces      : {len(sentence.replace(" ",""))}")
print(f"Total words         : {len(words)}")
print(f"Starts with cap     : {sentence.istitle()}")
>>>>>>> fab3683d8196c1621f5725473890127b19f45853
print(f"count of a          : {sentence.count("a")}")