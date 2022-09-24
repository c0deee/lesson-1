import re
val = input()
vowels = 'eyuioa'
consonants = 'qwrtpsdfghjklzxcvbnm'
print(len(re.findall(r'[a-z]{2}', val)))
print(len(re.findall(r'[A-Z]{2}', val)))
print(len(val))
print(len([x for x in val if x in vowels]))
print(len([x for x in val if x in consonants]))
