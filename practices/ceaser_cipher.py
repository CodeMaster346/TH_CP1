#TH 2nd Ceaser Cipher Practice

def encode(sentence):
    for char in sentence:
        new_letter_value = ord(f"{char}") + shift_number
        new_letter = chr(new_letter_value)

while True:
    sentence = input("Give me the sentence or phrase you want to encode/decode: ")
    encode_or_decode = int(input("1. Encode\n2. Decode\nGive me the number of the option you want to choose: "))