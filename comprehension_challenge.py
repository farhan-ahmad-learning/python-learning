list = [i for i in range(1, 50) if i % 3 == 0 and i % 5 == 0]
print(f"Divisble by 3 and 5: {list}")

words = ["apple", "banana", "elephant", "grape", "orange", "mango", "avocado"]
vowel = [i for i in words if i[0] in "aeiou"]
print(f"Vowel words: {vowel}")


celsius = [0, 10, 20, 30, 37, 40, 100]
fahrenheit = [(i * 9/5) + 32 for i in celsius]
print(f"Fahrenheit: {fahrenheit}")


keys = ["name", "age", "city", "job"]
values = ["Farhan", 35, "Delhi", "Localization"]
profile = {k: v for k, v in zip(keys, values)}
print(f"Profile: {profile}")


sentences = [
    "Python is amazing",
    "I love localization work",
    "AWS is the future",
    "Learning every day"
]
WC = {sent: len(sent.split()) for sent in sentences}
print(f"\nWord counts: ")
for sent, count in WC.items():
    print(f"    '{sent}' -> {count} words")