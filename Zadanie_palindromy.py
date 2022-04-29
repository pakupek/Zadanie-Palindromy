                              
'''
def palindrome(word_to_be_checked):
    word_to_be_checked = word_to_be_checked.lower()
    if word_to_be_checked == word_to_be_checked[::-1]:
        print('True')
    else:
        print('False')

palindrome(word_to_be_checked = 'Potop')
'''
'''
word_to_be_checked = 'Potop'
w = ''

for i in word_to_be_checked:
    word_to_be_checked = word_to_be_checked.lower()
    w = w.lower()
    w = i+w
if (word_to_be_checked == w):
    print('True')
else:
    print('False')
'''


