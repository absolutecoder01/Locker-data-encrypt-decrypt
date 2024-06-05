import pyAesCrypt
import time
from art import *
import sys
import os


def main():
  password()


def password():
  global password

  Art = text2art("Locker")
  print(Art)
  # print(Art)

  haslo = 'qwerty'

  password = input('Podaj hasło: ')
  if password != haslo:
    badpassword()

  else:
    wybor()


def option():
  odp = int(input("Chcesz spróbować jeszcze raz?: (1-Tak/0-Nie)"))
  if odp == 1:
    main()
  else:
    time.sleep(0.5)
    print("Zakończenie programu...")
    time.sleep(0.5)
    sys.exit()


def badpassword():
  print("Niepoprawne hasło!!!")
  main()


def wybor():

  global wybor

  time.sleep(0.5)
  print('1 - Zaszyfrować plik')
  time.sleep(0.5)
  print('2 - Odszyfrować plik')
  time.sleep(0.5)

  wybor = int(input('Podaj co chcesz zrobić?: '))

  if wybor == 1:
    zaszyfruj()
  elif wybor == 2:
    odszyfruj()
  else:
    print('Podaj poprawny wybór')
    wybor()


def zaszyfruj():
  pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)
  os.remove('data.txt')


def odszyfruj():
  pyAesCrypt.decryptFile('data.txt.aes', 'data_odszyfrowane.txt', password)
  # with open('data.txt', 'w') as f:
  #   f.write(data)
  #   f.


if __name__ == "__main__":
  main()
