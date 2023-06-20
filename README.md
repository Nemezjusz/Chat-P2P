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
Bezpieczna wymina wiadomości i plików w naszej aplikacji opiera sie na szyfrowaniu ich kluczem AES. Niestety pojawia się problem przekazania samego klucza. Problem rozwiązujemy dzięki algorytmowi RSA. Klucz AES szyfrujemy kluczem publicznym naszego peera, co pozwala mu na rozszyfrowanie go swoim kluczem prywatnym. W folderze [zadanie2](zadanie2) znajduje się zarówno zaszyfowany klucz AES jak i klucz prywatny. Użyj go aby rozszyfrować klucz AES a nastpnie postaraj się sprawdzić co kryje sie pod tajną wiadomościa: 
```python
tajna_wiadomosc = b'\xe3\x12\x1dOc\xe76e\x9a\xb6\x82\x10\x87E\xd3\xa8'
```
Oprócz funkcji takich jak *rsa.decrypt*, *AES.new()* (używamy trybu AES.MODE_ECB) przydatna bedzie taże funkcja *unpad()*. Potrzebujemy jej ponieważ algorytm AES szyfruje wiadomości w bloki po 16 bajtów. Jeśli wiadomość jest za krótka musimy ja uzupełnić putymi bajtami. Funkcja *unpad()* "wypakowuje" wiadomość z pustych bajtów.  

## Zadanie 3
**W tym i następnym zadaniu będziemy starać się zaimplementować bardzo uproszczony czat p2p, wszytkie wiadmosci beda wyswietlane w konsoli, bez enkrypcji**
Kod do uzupełnienia znajdziesz w folderze zadanie3.\
Peer dołączający do pokoju nie jest poprawnie skonfigurowany, Twoim zadaniem będzie uzupełnienie brakującego kodu w funkcji join_room() \
Podpowiedź:\
Przeanalizuj kod w funkcji create_room() mechanika wysyłania i odbierania wiadomości jest bardzo podobna\
Po poprawnym wykonaniu ćwiczenia po uruchomieniu dwóch terminali powinieneś nawiązać połączenie, ale jeszcze nie będziesz mógł wysyłać wiadomości 
## Zadanie 4
Jest to kontynuacja zadania 3.\ 
Program zadanie3 nadal nie działa poprawnie, nie możesz wysyłać wiadomości
Napraw problem tak aby komunikacja pomiędzy peerami (2 terminalami) byla możliwa.\
Kod uzupełnij w funkcji start_czat()\
posluz sie np \
While(true)\
Po poprawnym wykonaniu obu ćwiczeń powinieneś widzieć wiadomości przesyłane z jednego terminala na drugi.




