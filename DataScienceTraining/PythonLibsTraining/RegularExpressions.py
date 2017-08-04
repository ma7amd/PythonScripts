import re

sentance = "بسم الله الرحمن الرحيم"


# Using match([Pattern], [searching string])
# matching only from beginning and return string if happen.
match = re.match(r'[أ-ى]', sentance)
match = re.match(r'[أ-ى]*', sentance)
match = re.match(r'[أ-ى]*[ ]', sentance)
match = re.match(r'([أ-ى]*[ ])*', sentance)
match = re.match(r'([أ-ي]*[ ])*([أ-ي]*)*', sentance)
print(match)


sentance = "1 بسم الله الرحمن الرحيم"
# Using search([Pattern], [searching string])
# searching from beginning till the first occurrence
search = re.search(r'[أ-ى]', sentance)
print(search)


# Using sub([Pattern], [new replace], [searching string])
# searching for a pattern in string and replacing it with the new string in position 2
text = 'He is a good person'
name = 'Hassan'

new_text = re.sub(r'^[H]e', name, text)
print(new_text)


# way one to get the number
phone = "010-168-32446 # this is my phone number"
num = re.sub(r'#.*$', '', phone)
print(num)

# way two to get the number
num1 = re.match(r'[0-9]*-', phone)
num1 = re.match(r'([0-9]*-)*', phone)
num1 = re.match(r'([0-9]*-)*[0-9]*', phone)
print(num1)

# way three to get the number
num2 = re.sub(r'\D', '', phone)
print(num2)


details = 'My name is Muhammad; محمد , my phone number is 010002557485.'
number = re.search(r'[\d]+', details)
number = re.search(r'[0-9]+', details)
print(number)

# Using findall()
# search anywhere for a pattern
findd = re.findall(r'\w+', details)
print(findd)

arabicLetters = re.findall(r'[أ-ي]', details)
print(arabicLetters)

arabicWord = re.findall(r'[أ-ي]+', details)
print(arabicWord)