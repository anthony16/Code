name = raw_input('Write Text: ')

name = name.lower()

output = []

for character in name:
    number = ord(character) - 96
    output.append(number)
    
answer = (sum(output) / float(len(output)))

print answer