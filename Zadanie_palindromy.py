                                        #Zadanie: palindromy
#Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. 
#Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.
#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
#Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.
'''
def palindrome(word_to_be_checked):
    """
    Funkcja palindrome opiera sie na argumencie word_to_be_checked.
    Następnie zamienia duże litery na małe które zostały podane w argumencie.
    Jeżeli tego bym  nie zrobił to słowo Potop nie bedzie palindromem gdyż Potop != potoP.
    Warunek if sprawdza czy podane słowo w argumencie bedzie takie samo po przejsciu od końca.
    Jeżeli tak to wypisze na konsoli True, w przeciwnym wypadku False
    """
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
    """
    W tym sposobie wykorzystałem pętle for która przechodzi przez kolejne litery w zmiennej word_to_be_checked.
    Tak samo jak w pierwszym rozwiązaniu zamieniam dużą litere na małą.
    Każde przejście przez litere jest przypisywane do zmiennej 'w'która przechowa każdą litere ze zmiennej word_to_be_checked.
    Nastepnie warunkiem if sprawdzam czy podane słowo w zmiennej word_to_be_checked jest równe w utworzonej zmiennej 'w'.
    Jeżeli tak to wypisze na konsoli True, w przeciwnym wypadku False.
    To mój taki dodatkowy sposób na rozwiązanie zadania nie wykorzystując funkcji.
    Mam nadzieje że jest to w miare zrozumiałe :).
    """
    word_to_be_checked = word_to_be_checked.lower()
    w = w.lower()
    w = i+w
if (word_to_be_checked == w):
    print('True')
else:
    print('False')
'''


