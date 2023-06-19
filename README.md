## Zadanie 1
Na początek, aby móc dostrzec różnice i popracować na socketach wykonamy ćwiczenie ze zwykłym serwerem i klientem. Wykonamy prosty chat w konsoli.
W folderze [zadanie](zadanie) zanjduje się kod serwera i część kodu klinenta. Uzupełnij go zgodnie ze wskazówkami.
- Utwórz socket i połącz go z serwerm. Serwer nasłuchuje na porcie 1234. Socket utoworzysz za pomocą komendy: 
```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- Zaimplemrntuj wysyłanie wiadomości. Możesz to zrobi za pomocą prostej pętli. Widomość do socketa przekażesz za pomocą komendy:
```python
socket.sendall(('wiadomość').encode('utf-8'))
```
- Uruchom serwer i utworzonego klienta.
  
## Zadanie 2
- W folderze [zadanie1](zadanie1) znajdziesz kod, postaraj się go przeanalizować jest to bardzo uproszczony model czatu p2p.
  
Uruchom go odpalając dwa terminale (na jednym stwórz pokój i podaj port np 10 na drugim dołącz do pokoju wpisując swoje ip oraz port taki sam numer jak przy tworzeniu pokoju)
Program nie działa poprawnie (wiadomości nie docierają), w odpowiednim miejscu uzupełnij brakujący kod tak aby wiadmości mogły być przesyłane.

 
## Zadanie 3
W szyfrowaniu z kluczem asymetrycznym używamy dwóch kluczy: klucza publicznego i klucza prywatnego. Klucz publiczny służy do szyfrowania danych, a klucz prywatny do odszyfrowywania danych. Z nazwy klucz publiczny może być publiczny (może być wysłany do każdego, kto potrzebuje wysłać dane). Nikt nie ma twojego klucza prywatnego, więc nikt w środku nie może odczytać twoich danych.

- W folderze [zadanie2](zadanie2) znajaduje się schemat kodu Szyfrowania kluczem asymetrycznym.
- Twoim zadaniem jest zaszyfrowanie wiadomości a następnie jej odszyfrowanie

przydatne funkcje:
rsa.newkeys
rsa.ectrypt
encode()
rsa.decrypt



