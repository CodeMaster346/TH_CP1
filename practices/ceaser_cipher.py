#TH 2nd Ceaser Cipher Practice

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

#DEFINING the encode/decode function
def encode_or_decode(sentence):
    #SETTING up the result sentence
    result = ""
    #LOOPING code for every character in the sentence
    for char in sentence:
        #checking if character is in the alphabet
        if char.isalpha():
            #checking if character is uppercase
            if char.isupper():
                #ADDING the shifted character to the result sentence
                result += chr((ord(char) - 65 + shift_number) % 26 + 65)
            #checking if character is lowercase
            elif char.islower():
                #ADDING the shifted character to the result sentence
                result += chr((ord(char) - 97 + shift_number) % 26 + 97)
        #making sure all spaces and symbols stay the same
        else:
            #ADDING the origional character to the result sentence
            result += char
    #PRINTING result sentence, since i couldnt find another way to get the sentence to print well
    print(result)

#PROMPTING user to give a sentence to encode/decode and SETTING sentence AS that INPUT
sentence = input("Give me the sentence or phrase you want to encode/decode: ")
#PROMPTING user to choose to either encode or decode the sentence and SETTING encode_decode AS that INPUT
encode_decode = int(input("1. Encode\n2. Decode\nGive me the number of the option you want to choose: "))
#checking if encode_decode is EQUAL TO 1
if encode_decode == 1:
    #PROMPTING the user to enter a shift number for encoding and SETTING shift_number AS that INPUT
    shift_number = int(input("What number do you want to shift the sentence by? "))
    #RUNNING the encode/decode function
    encode_or_decode(sentence)
    #checking if encode_decode is EQUAL TO 2
elif encode_decode == 2:
    #PROMPTING the user to enter the negative version of the origional shift number and SETTING shift_number AS that INPUT
    shift_number = int(input("Give me the negative version of the origional shift number? "))  
    #RUNNING encode/decode function  
    encode_or_decode(sentence)