                                        #Zadanie: palindromy
#Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. 
#Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.
#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
#Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.

def palindrome(word_to_be_checked):
    word_to_be_checked = word_to_be_checked.lower()
    if word_to_be_checked == word_to_be_checked[::-1]:
        print('True')
    else:
        print('False')

palindrome(word_to_be_checked = 'Potop')