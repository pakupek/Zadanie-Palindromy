# Zadanie-Palindromy
PL:

Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. 
Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.
Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.


W pierwszym sposobie Funkcja palindrome opiera sie na argumencie word_to_be_checked.
Następnie zamienia duże litery na małe które zostały podane w argumencie.
Jeżeli tego bym  nie zrobił to słowo Potop nie bedzie palindromem gdyż Potop != potoP.
Warunek if sprawdza czy podane słowo w argumencie bedzie takie samo po przejsciu od końca.
Jeżeli tak to wypisze na konsoli True, w przeciwnym wypadku False


W drugim sposobie wykorzystałem pętle for która przechodzi przez kolejne litery w zmiennej word_to_be_checked.
Tak samo jak w pierwszym rozwiązaniu zamieniam dużą litere na małą.
Każde przejście przez litere jest przypisywane do zmiennej 'w'która przechowa każdą litere ze zmiennej word_to_be_checked.
Nastepnie warunkiem if sprawdzam czy podane słowo w zmiennej word_to_be_checked jest równe w utworzonej zmiennej 'w'.
Jeżeli tak to wypisze na konsoli True, w przeciwnym wypadku False.
To mój taki dodatkowy sposób na rozwiązanie zadania nie wykorzystując funkcji.
Mam nadzieje że jest to w miare zrozumiałe :).


ENG:
##The Palindromes Quest
Your task will be to write a function that checks if a given word is a palindrome.
A palindrome is a word that sounds the same when read from left to right and right to left. Examples include "canoe" and "deluge".
Program a function that takes one string argument and returns a boolean: True / False value that tells you whether the given text is a palindrome.
Remember that string / text is a collection of characters. You are already familiar with collection functions that allow you to refer to elements indexed from the beginning and from the end.


In the first way, the palindrome function relies on the argument word_to_be_checked.
Then it converts uppercase letters to lowercase letters that were given in the argument.
If I did not do this, the word Flood would not be a palindrome because Flood! = Flood.
The if condition checks that the given word in the argument will be the same after going from the end.
If so, it will print True on the console, False otherwise


In the second method, I used a for loop that goes through the letters in the variable word_to_be_checked.
As in the first solution, I change the capital letter to lower case.
Each letter pass is assigned to the variable 'w' which will hold each letter in word_to_be_checked.
Then with the if condition I check if the given word in the variable word_to_be_checked is equal to the created variable 'w'.
If so, it will print True on the console, False otherwise.
This is my additional way of solving a task without using a function.
I hope it is reasonably understandable :).
