print("Welcome to Oxford Recruitment System we will be asking you a set of questions so please answer them.")
print("What's your name?")
name = input()
print("How old are you?")
age = input()
print("Which subject do you choose?")
subject = input()
def ceasarEncrypt(message, shift):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) + shift) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return result

filename = "%s.txt" % name
message = "Oxford Recruitment System\nWhat's your name?\n%s\nHow old are you?\n%s\nWhich subject do you choose?\n%s\n" %(name,age,subject)
encryptedmessage = ceasarEncrypt(message, 3)
f = open(filename, 'w')
f.write(encryptedmessage)
f.close()
print(message)



def ceasarDecrypt(message, shift):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - shift) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return result
