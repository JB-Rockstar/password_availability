import re
import easygui

password = easygui.passwordbox("Password Rules:\n Your password should have:\n - Minimum of 8 characters,\n - At least one uppercase English letter,\n - At least one lowercase English letter,\n - At least one digit,\n - At least one of these special characters: #?!@$%^&*-\n \n Now, please choose a new password:\n")
pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
pw = pattern.search(password)

while True:

    if pw is not None:
        print('Greetings!!')
        break

    while pw is None or pw == '':
        password = easygui.passwordbox("Wrong Selection! Please choose a suitable password: \n")
        pw = pattern.search(password)

    if pw is not None:
        print('Welcome!')
        break

# JB-Rockstar
# gokhanbalik8@gmail.com
