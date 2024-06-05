# Locker-data-encrypt-decrypt
Prosty program do szyfrowania i deszyfrowania pliku tekstowego.

## Instalacja

Będą potrzebne 2 dodatkowe biblioteki:

```bash
  pip install pyAesCrypt
  pip install art
```

## Korzystanie 

Uruchamiamy plik main.py i gotowe! Wystarczy wpisać hasło: qwerty

![image](https://github.com/absolutecoder01/Locker-data-encrypt-decrypt/assets/156543239/15b341a0-bc65-4e55-b8b0-bb67ecef0dba)

## Szyfrowanie

Aby program działał musi istnieć plik data.txt, i najlepiej wpisane w nim dane do zaszyfrowania

![image](https://github.com/absolutecoder01/Locker-data-encrypt-decrypt/assets/156543239/512152a2-5a4b-4158-a372-68895963a79d)

Opcja 1 - szyfruje plik z danymi za pomocą algorytmu AES-256, i tym samym powstaje plik data.txt.aes który jest zaszyfrowany:
![image](https://github.com/absolutecoder01/Locker-data-encrypt-decrypt/assets/156543239/429f2390-cd21-40da-87bc-e1deb92fe47c)

Opcja 2 - deszyfruje plik data.txt.aes w data_odszyfrowane.txt:

![image](https://github.com/absolutecoder01/Locker-data-encrypt-decrypt/assets/156543239/9ad0f966-4fb1-4d65-bb83-6c4ca1bfdefb)


