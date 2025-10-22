#TH 2nd Ceaser Cipher Practice

#CONTAINER that holds the different characters set to variable new_letter

#DEFINE the FUNCTION for encoding which needs the VARIABLE sentence
#   FOR every character in the VARIABLE sentence
#       IF charater IS a letter THEN
#           SET new_letter_value AS the ASCII version of that character PLUS the shift number
#           SET new_letter AS the LETTER version of new_letter_value
#           ADD new_letter to CONTAINER
#       ELSE
#           ADD character to CONTAINER

#DEFINE the FUNCTION for decoding which needs the VARIABLE sentence
#   SET instance AS 1
#   LOOP that runs 26 times   
#       FOR every character in the VARIABLE sentence
#           IF character IS A or a
#               
#           ELSE, IF charater IS a letter THEN
#               SET new_letter_value AS the ASCII version of that character MINUS instance
#               SET new_letter AS the LETTER version of new_letter_value
#               ADD new_letter to CONTAINER
#           ELSE
#               ADD character to CONTAINER
#               SET instance AS instance + 1

#PROMPT user to enter the sentence they want to encode/decode
#SET sentence AS the INPUT the user gives
#PROMPT user to enter the option to encode or decode the sentence
#SET encode_or_decode AS the INPUT the user gives
#IF encode_or_decode IS SET AS 1 THEN
#   PROMPT user to give what number they want to shift by
#   SET shift_number AS the INPUT the user gives
#   RUN encode FUNCTION
#   DISPLAY the contents of the CONTAINER
#ELSE, IF encode_or_decode IS SET AS 2 THEN
#   RUN decode FUNCTION
#   DISPLAY the contents of the CONTAINER
newSentenceList = []


def encode(sentence):
    for char in sentence:
        if char.isalpha():
            new_letter_value = ord(f"{char}") + shift_number
            new_letter = chr(new_letter_value)
            newSentenceList.append(new_letter)
        else:
            newSentenceList.append(char)

sentence = input("Give me the sentence or phrase you want to encode/decode: ")
encode_or_decode = int(input("1. Encode\n2. Decode\nGive me the number of the option you want to choose: "))
if encode_or_decode == 1:
    shift_number = int(input("What number do you want to shift the sentence by(Max number is 26)? "))
    encode(sentence)
    new_sentence = ''.join(newSentenceList)
    print(new_sentence)
elif encode_or_decode == 2:
