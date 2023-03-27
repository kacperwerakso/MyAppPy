import random
import datetime
import requests
import random
import webbrowser
from pathlib import Path

login = 0
haslo = 0
def rejestracja():
    print("\n0. Wyjście\n1. Rejestracja\n2. Logowanie\n")
    while True:
        x = input("Co chcesz zrobić?: \n")
        if x == "1":
            rejlogin = input("Utwórz login: ")
            rejhaslo = input("Utwórz haslo: ")
            rehaslo = input("Powtórz haslo: ")
            if (rejhaslo == rehaslo): 
                print("\n--- POMYŚLNIE UTWORZONO KONTO ---\n")
                with open("MyAppPy/konta.txt", "a", encoding="UTF-8") as plik:
                    plik.write(f"{rejlogin, rejhaslo}")
                return rejestracja()
            else: 
                print("\nBłąd")
                return rejestracja()
        elif x == "2":
            global login
            global haslo
            login = input("Podaj login: ")
            haslo = input("Podaj hasło: ")
            with open("MyAppPy/konta.txt") as plik1:
                if login and haslo in plik1.read():
                    print("\n--- POMYŚLNIE ZALOGOWANO ---\n")
                    return menu1()                
                else:
                    print("\nBłąd")
                    return rejestracja()
        elif x == "0":
            return menu()
        else:
            print("\nBłąd")
            return rejestracja()



def calc():
    while(True):
        print("\n0. Wyjście\n1. Dodawanie\n2. Odejmowanie\n3. Mnozenie\n4. Dzielenie\n5. Potęgowanie\n")
        z = input("Co chcesz zrobić: ")
        if z == "0":
            with open("MyAppPy/konta.txt") as plik1:
                if login and haslo in plik1.read():
                    return menu1()
                else:
                    return menu()
        try:
            x = int(input("Podaje pierwszą liczbę: "))
            y = int(input("Podaje drugą liczbę: "))
        except ValueError:
                print("\nBłąd\n")
                continue

    
        if z == "1":
            print("\nWynik dodawania: ",x + y) 
        elif z == "2":
            print("\nWynik odejmowania: ",x - y)
        elif z == "3":
            print("\nWynik mnozenia: ",x * y)
        elif z == "4":
            if x == 0 or y == 0:
                print("\nBłąd dzielenia przez 0")
            else:
                print("\nWynik dzielenia: ",x / y)
        elif z == "5":
            print("\nWynik potęgowania: ",x ** y)
        else:
            print("\nBłąd")
            return calc()





def data_czas():
    datetime.datetime.now()
    print("\nAktualna data i godzina: ",datetime.datetime.now())
    while(True):
        x = input("\n0. Wyjdź\n1. Odświerz\n")
        if x == "0":
           with open("MyAppPy/konta.txt") as plik1:
                if login and haslo in plik1.read():
                    return menu1()
                else:
                    return menu()
        if x == "1":
          return data_czas()
        else:
          continue



def zgadywanie():
    while(True):
        liczba = random.randint(1, 10)
        try:
            odp = int(input("\nZgadnij losową liczbę od 1 do 10: "))
            print("\n0 - Wyjscie\n")
        except ValueError:
            print("\nBłąd")

            print("\n0 - Wyjscie\n")
            continue

        if liczba == odp:
            try:
                print("\nZGADŁEŚ!")
                continue
            except ValueError:
                print("Błąd")
                continue
        elif odp == 0:
            with open("MyAppPy/konta.txt") as plik1:
                if login and haslo in plik1.read():
                    return menu1()
                else:
                    return menu()
        else:
            print("\nNIE ZGADŁEŚ, spróbuj ponownie")
            return zgadywanie()


definicje = {}
def slownik():
    while(True):
        print("\n1. Dodaj definicje")
        print("2. Znajdz definicje")
        print("3. Usun definicje")
        print("0. Wyjście")
        wybor = input("\nCo chcesz zrobic?: ")

        if wybor == "1":
            klucz = input("Podaj slowo: ")
            definicja = input("Podaj definicje tego slowa: ")
            definicje[klucz] = definicja
            print("\nDODANO DEFINICJĘ\n")
        elif wybor == "2":
            klucz = input("Podaj szukana definicje: ")
            if klucz in definicje:
                print(definicje[klucz])
            else:
                print("\nNIE ZNALEZIONO", klucz)
        elif wybor == "3":
            klucz = input("Ktora definicje chcesz usunac?: ")
            if klucz in definicje:
                del definicje[klucz]
                print("\nUSUNIĘTO DEFINICJĘ", klucz)
            else:
                print("\nNIE ZNALEZIONO", klucz)
        elif wybor == "0":
                    return menu1()
        else:
            print("\nPOZA ZAKRESEM\n")
            return slownik()
                        







def orzel_reszka():
    orzelreszka = ["\nOrzeł", "\nReszka"]
    print(random.choice(orzelreszka))
    while(True):
        x = input("\n0. Wyjdź\n1. Rzuć monetą\n")
        if x == "1":
          return orzel_reszka()
        elif x == "0":
           with open("MyAppPy/konta.txt") as plik1:
                if login and haslo in plik1.read():
                    return menu1()
                else:
                    return menu()
        else:
          continue


def bety():
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
                    with open("MyAppPy/konta.txt") as plik1:
                        if login and haslo in plik1.read():
                            return menu1()
                        else:
                            return menu()
        elif y == 0:
                    with open("MyAppPy/konta.txt") as plik1:
                        if login and haslo in plik1.read():
                            return menu1()
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
    w = input("Co chcesz zrobić?: ")
    if w == "0":
        with open("MyAppPy/konta.txt") as plik1:
            if login and haslo in plik1.read():
                return menu1()
            else:
                return menu()
    elif w == "1":
        try:
            y = float(input("\nPodaj stopnie Celcjusza: "))
            print("\n",y, "to", y * 1.8 + 32, "Fahrenheitow")
            continue
        except ValueError:
            print("\nBłąd\n")
            continue
    elif w == "2":
        try:
            y = float(input("\nPodaj stopnie Celcjusza: "))
            print("\n",y, "to", y + 273.15, "Kelwinow")
            continue
        except ValueError:
            print("\nBłąd\n")
            continue
    else:
        continue






def rzuty():
    while(True):
        print("\nWylosowałeś: ", random.randint(1, 6))
        x = input("\n1. Rzuć\n0. Wyjście\n")
        if x == "1":
            return rzuty()
        elif x == "0":
            with open("MyAppPy/konta.txt") as plik1:
                if login and haslo in plik1.read():
                    return menu1()
                else:
                    return menu()
        else:
            continue


def avatar():
    while(True):
        x = input("0. Wyjście\n1. Wylosuj avatar\n")
        if x == "1":
            response = requests.get(f"https://avatars.dicebear.com/api/male/{random.random()}.svg")

            Path("MyAppPy/avatars").mkdir(exist_ok = True) 

            with open("MyAppPy/avatars/avatar.svg", "wb") as file: 
                file.write(response.content)
            print("Pomyślnie ustawiono nowy avatar")
        if x == "0":
            return menu1()
        else:
            return avatar()


def wyszukiwarka():
    h = input("\n0. Wyjście\n1. Wyszukaj\n")
    if h == "0":
        with open("MyAppPy/konta.txt") as plik1:
            if login and haslo in plik1.read():
                return menu1()
            else:
                return menu()
    elif h == "1":
        szukana = input("Wpisz stronę internetową: ")
        webbrowser.open(szukana)
        return wyszukiwarka()
    else:
        return wyszukiwarka()





def menu():
    while(True):
        print("\n+------ WITAJ W APLIKACJI MyAppPY ------+")
        print("|                                       |\n|                                       |\n+---------------- KONTO ----------------+\n|                                       |\n|  1.  Utwórz konto/zaloguj             |\n|                                       |\n+-------------- NARZĘDZIA --------------+")
        print("|                                       |\n|  2.  Kalkulator                       |\n|  3.  Wyszukiwarka internetowa         |\n|  4.  Tłumacz kursów/betów             |\n|  5.  Przelicznik temperatur           |\n|  6.  Aktualna data i godzina          |")
        print("|                                       |\n+----------------- GRY -----------------+")
        print("|                                       |\n|  7. Gra - Zgadnij liczbę              |\n|  8. Gra - Orzeł czy reszka            |\n|  9. Gra - Rzut kością                 |\n|                                       |")
        print("+---------------------------------------+")
        print("|                                       |\n|  0. Wyłącz aplikację                  |\n|                                       |")
        print("+---------------------------------------+\n")
        y = input("\nWybierz czynność(numer):  ")
        if y == "0":
            break
        elif y == "2":
            return calc()
        elif y == "9":
            return rzuty()
        elif y == "4":
            return bety()
        elif y == "5":
            return temperature()
        elif y == "8":
            return orzel_reszka()
        elif y == "7":
            return zgadywanie()
        elif y == "6":
            return data_czas()
        elif y == "1":
            return rejestracja()
        elif y == "3":
            return wyszukiwarka()    
        else:
            continue


def menu1():
    while(True):
        print("\n+------ WITAJ W APLIKACJI MyAppPY ------+")
        print("|                                       |\n|                                       |\n+---------------- KONTO ----------------+\n|                                       |\n|  1.  Usuń konto                       |\n|  2.  Avatar                           |\n|  3.  Notatnik                         |\n|                                       |\n+-------------- NARZĘDZIA --------------+")
        print("|                                       |\n|  4.  Kalkulator                       |\n|  5.  Wyszukiwarka internetowa         |\n|  6.  Tłumacz kursów/betów             |\n|  7.  Przelicznik temperatur           |\n|  8.  Aktualna data i godzina          |")
        print("|                                       |\n+----------------- GRY -----------------+")
        print("|                                       |\n|  9. Gra - Zgadnij liczbę              |\n| 10. Gra - Orzeł czy reszka            |\n| 11. Gra - Rzut kością                 |\n|                                       |")
        print("+---------------------------------------+")
        print("|                                       |\n|  0. Wyłącz aplikację                  |\n|                                       |")
        print("+---------------------------------------+\n")
        y = input("\nWybierz czynność(numer):  ")
        if y == "0":
            break
        elif y == "4":
            return calc()
        elif y == "11":
            return rzuty()
        elif y == "6":
            return bety()
        elif y == "7":
            return temperature()
        elif y == "10":
            return orzel_reszka()
        elif y == "3":
            return slownik()
        elif y == "9":
            return zgadywanie()
        elif y == "8":
            return data_czas()
        elif y == "2":
            return avatar()
        elif y == "5":
            return wyszukiwarka()
        elif y == "1" :
            print("\n--- POMYŚLNIE WYLOGOWANO ---")
            open("MyAppPy/konta.txt", "w").close
            return menu()   
        else:
            continue


odpowiedz = menu()
print(odpowiedz)
