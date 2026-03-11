print( 'Two-letter domain names:' )

letter1 = 'a'
letter2 = 'a'

while letter1 <= 'z':
    while letter2 <= 'z':
        print(f'{letter1}{letter2}.com')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)
# Outer Loop
# Inner loop