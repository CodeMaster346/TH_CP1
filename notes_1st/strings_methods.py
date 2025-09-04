# TH 2nd strings methods notes

name = input("What is your name? ").strip().capitalize()
age = float(input("How old are you? "))
print(f"Hello {name}, nice to meet you! I cant believe you are {age:.1f}.")
age = input("How old are you? ")
print(age.isdigit())
print("Really? " + age + " is old?")
sentence = "The quick brown fox jumps over the lazy dog. "
word = "fox"
start = sentence.find(word)
length = len(word)
print(sentence.replace(word, "yellow"))
