<h1>This is the Oxford Recruitment System</h1> 

Here you will be able to fill out a form and hand it into where you need. Its fast and simple.

<img src="logo.PNG" alt="Screen from system">

```python
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
```

Here are some stuff you will need to fill out:
```python
print("Welcome to Oxford Recruitment System we will be asking you a set of questions so please answer them.")
print("What's your name?")
name = input()
print("How old are you?")
age = input()
print("Which subject do you choose?")
subject = input()
```
Also:
```python
you will be able to encrypt and decrypt your message before sending incase
you are worried it will get stolen.
```

License(Please read if you are unsure of anything...)
[CLICK HERE!!](https://choosealicense.com/licenses/mit/)
