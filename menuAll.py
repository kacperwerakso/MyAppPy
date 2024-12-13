import random
import datetime
import requests
import random
import webbrowser
from pathlib import Path

login = 0
password = 0
def registration():
    print("\n0. Wyjście\n1. Rejestracja\n2. Logowanie\n")
    while True:
        question = input("Co chcesz zrobić?: \n")
        if question == "1":
            reglogin = input("Utwórz login: ")
            regPassword = input("Utwórz haslo: ")
            rehaslo = input("Powtórz haslo: ")
            if (regPassword == rehaslo): 
                print("\n--- POMYŚLNIE UTWORZONO KONTO ---\n")
                with open("accounts.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{reglogin, regPassword}")
                return registration()
            else: 
                print("\nBłąd")
                return registration()
        elif question == "2":
            global login
            global password
            login = input("Podaj login: ")
            password = input("Podaj hasło: ")
            with open("accounts.txt") as file:
                if login and password in file.read():
                    print("\n--- POMYŚLNIE ZALOGOWANO ---\n")
                    return menuAfterLogin()                
                else:
                    print("\nBłąd")
                    return registration()
        elif question == "0":
            return menu()
        else:
            print("\nBłąd")
            return registration()

class MenuCreator:
    @staticmethod
    def menuHtml():
        print("\n--- Utwórz plik HTML z wybraną treścią ---\n")
        choice = input("\n0. Wyjście\n1. Utwórz stronę\n")
        if choice == "1":
            InputHtml().enterPrompt()
        elif choice == "0":
            with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        else:
            return MenuCreator().menuHtml()



class InputHtml:
    @staticmethod
    def enterPrompt():
        print("\n----- POMYŚLNIE ROZPOCZĘTO TWORZENIE STRONY -----\n\n")
        title = input("Wprowadź treść nagłówka na stronie: ")
        titleColor = input("Wybierz kolor nagłówka (j. ang): ")
        text = input("Wprowadź treść pod nagłówkiem: ")
        textColor = input("Wybierz kolor treści (j. ang): ")
        backgroundColor = input("Wybierz tło strony (j. ang): ")
        nameOfFile = input("Nazwa pliku przechowującego stronę: ")
        fullNameOfFile = open(f"{nameOfFile}.html", "w")
        fullNameOfFile.write(f"<html>\n<head>\n<title>Tresc do HTML</title>\n</head> <body bgcolor={backgroundColor}> <h1><font color={titleColor}><center><br><br>{title}</center></font></h1>\n<center><p><br><br><font color={textColor}>{text}</font></p></center>\n</body></html>")
        fullNameOfFile.close()
        lastQuestion = input("\n----- POMYŚLNIE UKOŃCZONO TWORZENIE STRONY -----\n\n0. Wyjście\n1. Stwórz kolejny\n")
        if lastQuestion == "1":
            return MenuCreator().menuHtml()
        elif lastQuestion == "0":
            with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        else:
            return MenuCreator().menuHtml()

activation = MenuCreator()


def calculator():
    while(True):
        print("\n0. Wyjście\n1. Dodawanie\n2. Odejmowanie\n3. Mnozenie\n4. Dzielenie\n5. Potęgowanie\n")
        question = input("Co chcesz zrobić?: ")
        if question == "0":
            with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        try:
            x = int(input("Podaje pierwszą liczbę: "))
            y = int(input("Podaje drugą liczbę: "))
        except ValueError:
                print("\nBłąd\n")
                continue

    
        if question == "1":
            print("\nWynik dodawania: ",x + y) 
        elif question == "2":
            print("\nWynik odejmowania: ",x - y)
        elif question == "3":
            print("\nWynik mnozenia: ",x * y)
        elif question == "4":
            if x == 0 or y == 0:
                print("\nBłąd dzielenia przez 0")
            else:
                print("\nWynik dzielenia: ",x / y)
        elif question == "5":
            print("\nWynik potęgowania: ",x ** y)
        else:
            print("\nBłąd")
            return calculator()





def dataTime():
    datetime.datetime.now()
    print("\nAktualna data i godzina: ",datetime.datetime.now())
    while(True):
        question = input("\n0. Wyjdź\n1. Odświerz\n")
        if question == "0":
           with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        if question == "1":
          return dataTime()
        else:
          continue



def guess():
    while(True):
        chosenNumber = random.randint(1, 10)
        try:
            answear = int(input("\nZgadnij losową liczbę od 1 do 10: "))
            print("\n0 - Wyjscie\n")
        except ValueError:
            print("\nBłąd")

            print("\n0 - Wyjscie\n")
            continue

        if chosenNumber == answear:
            try:
                print("\nZGADŁEŚ!")
                continue
            except ValueError:
                print("Błąd")
                continue
        elif answear == 0:
            with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        else:
            print("\nNIE ZGADŁEŚ, spróbuj ponownie")
            return guess()


definition = {}
def dictionary():
    while(True):
        print("\n1. Dodaj definicje")
        print("2. Znajdz definicje")
        print("3. Usun definicje")
        print("0. Wyjście")
        choice = input("\nCo chcesz zrobic?: ")

        if choice == "1":
            key = input("Podaj slowo: ")
            definitions = input("Podaj definicje tego slowa: ")
            definition[key] = definitions
            print("\nDODANO DEFINICJĘ\n")
        elif choice == "2":
            key = input("Podaj szukana definicje: ")
            if key in definition:
                print(definition[key])
            else:
                print("\nNIE ZNALEZIONO", key)
        elif choice == "3":
            key = input("Ktora definicje chcesz usunac?: ")
            if key in definition:
                del definition[key]
                print("\nUSUNIĘTO DEFINICJĘ", key)
            else:
                print("\nNIE ZNALEZIONO", key)
        elif choice == "0":
                    return menuAfterLogin()
        else:
            print("\nPOZA ZAKRESEM\n")
            return dictionary()
                        



def headsTails():
    orzelreszka = ["\nOrzeł", "\nReszka"]
    print(random.choice(orzelreszka))
    while(True):
        question = input("\n0. Wyjdź\n1. Rzuć monetą\n")
        if question == "1":
          return headsTails()
        elif question == "0":
           with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        else:
          continue


def bets():
    print("\nWitaj w tłumaczu kursów/betów")
    while(True):
        try:
            x = float(input("\nPodaj kurs pierwszego zawodnika/drużyny: "))
            y = float(input("Podaj kurs drugiego zawodnika/drużyny: "))
            print("\n0 - Wyjście")
        except ValueError:
                print("\nBłąd")
                continue
        if x == 0:
            with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        elif y == 0:
            with open("accounts.txt") as file1:
                if login and password in file1.read():
                    return menuAfterLogin()
                else:
                    return menu()
        elif x < y:
            print("\nLudzie obstawiają zawodnika z kursem", x, "i jest bardziej prawdopodobne, że wygra z zawodnikiem z kursem", y)

        elif x == y:
            print("\nSzanse są wyrównane")

        else:  
            print("\nLudzie obstawiają zawodnika z kursem", y, "i jest bardziej prawdopodobne, że wygra z zowodnikiem z kursem", x)
            





def temperature():
  while(True):
    print("\n0. Wyjście\n1. Celcjusze na Fahrenheity\n2. Celcjusze na Kelwiny\n")
    question = input("Co chcesz zrobić?: ")
    if question == "0":
        with open("accounts.txt") as file:
            if login and password in file.read():
                return menuAfterLogin()
            else:
                return menu()
    elif question == "1":
        try:
            y = float(input("\nPodaj stopnie Celcjusza: "))
            print("\n",y, "to", y * 1.8 + 32, "Fahrenheitow")
            continue
        except ValueError:
            print("\nBłąd\n")
            continue
    elif question == "2":
        try:
            y = float(input("\nPodaj stopnie Celcjusza: "))
            print("\n",y, "to", y + 273.15, "Kelwinow")
            continue
        except ValueError:
            print("\nBłąd\n")
            continue
    else:
        continue






def throw():
    while(True):
        print("\nWylosowałeś: ", random.randint(1, 6))
        answer = input("\n1. Rzuć\n0. Wyjście\n")
        if answer == "1":
            return throw()
        elif answer == "0":
            with open("accounts.txt") as file:
                if login and password in file.read():
                    return menuAfterLogin()
                else:
                    return menu()
        else:
            continue


def avatar():
    while(True):
        draw = input("0. Wyjście\n1. Wylosuj avatar\n")
        if draw == "1":
            response = requests.get(f"https://avatars.dicebear.com/api/male/{random.random()}.svg")

            Path("avatars").mkdir(exist_ok = True) 

            with open("avatars/avatar.svg", "wb") as file: 
                file.write(response.content)
            print("Pomyślnie ustawiono nowy avatar")
        if draw == "0":
            return menuAfterLogin()
        else:
            return avatar()


def webBrowse():
    browse = input("\n0. Wyjście\n1. Wyszukaj\n")
    if browse == "0":
        with open("accounts.txt") as file:
            if login and password in file.read():
                return menuAfterLogin()
            else:
                return menu()
    elif browse == "1":
        search = input("Wpisz stronę internetową: ")
        webbrowser.open(search)
        return webBrowse()
    else:
        return webBrowse()





def menu():
    while(True):
        print("\n+------ WITAJ W APLIKACJI MyAppPY ------+")
        print("|                                       |\n|                                       |\n+---------------- KONTO ----------------+\n|                                       |\n|  1.  Utwórz konto/zaloguj             |\n|                                       |\n+-------------- NARZĘDZIA --------------+")
        print("|                                       |\n|  2.  Kalkulator                       |\n|  3.  Wyszukiwarka internetowa         |\n|  4.  Tłumacz kursów/betów             |\n|  5.  Przelicznik temperatur           |\n|  6.  Aktualna data i godzina          |\n|  7.  Utwórz HTML                      |")
        print("|                                       |\n+----------------- GRY -----------------+")
        print("|                                       |\n|  8. Gra - Zgadnij liczbę              |\n|  9. Gra - Orzeł czy reszka            |\n|  10. Gra - Rzut kością                |\n|                                       |")
        print("+---------------------------------------+")
        print("|                                       |\n|  0. Wyłącz aplikację                  |\n|                                       |")
        print("+---------------------------------------+\n")
        whatToDo = input("\nWybierz czynność(numer):  ")
        if whatToDo == "0":
            return "DO ZOBACZENIA!"
        elif whatToDo == "2":
            return calculator()
        elif whatToDo == "9":
            return headsTails()
        elif whatToDo == "4":
            return bets()
        elif whatToDo == "5":
            return temperature()
        elif whatToDo == "8":
            return guess()
        elif whatToDo == "7":
            return activation.menuHtml()
        elif whatToDo == "6":
            return dataTime()
        elif whatToDo == "1":
            return registration()
        elif whatToDo == "3":
            return webBrowse()
        elif whatToDo == "10":
            return throw()   
        else:
            continue


def menuAfterLogin():
    while(True):
        print("\n+------ WITAJ W APLIKACJI MyAppPY ------+")
        print("|                                       |\n|                                       |\n+---------------- KONTO ----------------+\n|                                       |\n|  1.  Usuń konto                       |\n|  2.  Avatar                           |\n|  3.  Notatnik                         |\n|                                       |\n+-------------- NARZĘDZIA --------------+")
        print("|                                       |\n|  4.  Kalkulator                       |\n|  5.  Wyszukiwarka internetowa         |\n|  6.  Tłumacz kursów/betów             |\n|  7.  Przelicznik temperatur           |\n|  8.  Aktualna data i godzina          |\n|  9.  Utwórz HTML                      |")
        print("|                                       |\n+----------------- GRY -----------------+")
        print("|                                       |\n|  10. Gra - Zgadnij liczbę             |\n|  11. Gra - Orzeł czy reszka           |\n|  12. Gra - Rzut kością                |\n|                                       |")
        print("+---------------------------------------+")
        print("|                                       |\n|  0. Wyłącz aplikację                  |\n|                                       |")
        print("+---------------------------------------+\n")
        whatToDo = input("\nWybierz czynność(numer):  ")
        if whatToDo == "0":
            return "DO ZOBACZENIA!"
        elif whatToDo == "4":
            return calculator()
        elif whatToDo == "12":
            return throw()
        elif whatToDo == "6":
            return bets()
        elif whatToDo == "7":
            return temperature()
        elif whatToDo == "11":
            return headsTails()
        elif whatToDo == "3":
            return dictionary()
        elif whatToDo == "10":
            return guess()
        elif whatToDo == "8":
            return dataTime()
        elif whatToDo == "2":
            return avatar()
        elif whatToDo == "9":
            return activation.menuHtml()
        elif whatToDo == "5":
            return webBrowse()
        elif whatToDo == "1" :
            print("\n--- POMYŚLNIE WYLOGOWANO ---")
            open("accounts.txt", "w").close
            return menu()   
        else:
            continue


activationMenu = menu()
print(activationMenu)
