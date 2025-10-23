#TH 2nd Ceaser Cipher Practice

#CONTAINER that holds the different characters set to variable new_letter

#DEFINE encode/decode function
#    SET up a result sentence
#    FOR every character IN the VARIABLE sentence
#        IF character is in the alphabet THEN
#            IF character is uppercase
#                ADD the shifted uppercase character to the result sentence
#            ELSE, IF character is lowercase THEN
#                ADD the shifted lowercase character to the result sentence
#        ELSE, if the alphabet check condition is not met
#            ADD character to result sentence
#    DISPLAY result sentence

#PROMPT user to enter the sentence they want to encode/decode
#SET sentence AS the INPUT the user gives
#PROMPT user to enter the option to encode or decode the sentence
#SET encode_decode AS the INPUT the user gives
#IF encode_decode IS SET AS 1 THEN
#   PROMPT user to give what number they want to shift by
#   SET shift_number AS the INPUT the user gives
#   RUN encode FUNCTION
#ELSE, IF encode_or_decode IS SET AS 2 THEN
#   PROMPT user to give the negative version of the origional shift number
#   SET shift_number AS the INPUT the user gives
#   RUN decode function
newSentenceList = []

def encode_or_decode(sentence):
    result = ""
    for char in sentence:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift_number) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + shift_number) % 26 + 97)
        else:
            result += char
    print(result)

sentence = input("Give me the sentence or phrase you want to encode/decode: ")
encode_decode = int(input("1. Encode\n2. Decode\nGive me the number of the option you want to choose: "))
if encode_decode == 1:
    shift_number = int(input("What number do you want to shift the sentence by? "))
    encode_or_decode(sentence)
elif encode_decode == 2:
    shift_number = int(input("Give me the negative version of the origional shift number? "))    
    encode_or_decode(sentence)