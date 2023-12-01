## P2P
Na czym polega peer to peer?
Peer-to-peer (P2P) to model komunikacji komputerowej oparty na idei decentralizacji. Sieć P2P w przeciwieństwie do tradycyjnego modelu serwer-klient, umożliwia interakcje i wymianę danych wprost między wszystkimi użytkownikami

## Chat P2P
Stworzona przez nas aplikacja służy do bezpośredniej komunikacji hostów (bez użycia serwera) w danej sieci lokalnej. 
Pozwala ona na wymiane wiadomości tekstowych jak i zarówno wymiane plików bez względu na ich rozszerzenie czy rozmiar(?).
Osiagamy to za pomocą operacji na socketach(...). 
Wymiana wiadomości jest dodatkowo enkryptowana za pomocą szyfru blokowego **AES w trybie ECB**. Klucz wymieniany jest za 
pomocą asymetrycznego algorytmu **RSA** co zapewnia ochrone przed jego przejęciem. GUI zostało wykonane za pomocą biblioteki 
**PyQt5** i zawartego w niej narzędzia Designer.

![obraz](https://github.com/Nemezjusz/Chat-P2P/assets/50834734/1a6b0313-d7ea-42d4-91e7-968f87e4c063)

Na załączonym obrazie możemy zaobserwować ustanowione połączenie i fragment konwersacji na dwóch instancjach aplikacji. 
Jak widać wymiana wiadomości odbywa się bezproblemowo i bezpiecznie. Wysyłanie, w tym przypadku obraz także powiodło się bez żadnych strat czy błędów.
Dodatkowo w lewej części wyświetlają nam sie informacje opisujące miedzy innymi status połączenia.

### Instrukcja obsługi aplikacji
Przed rozpoczęciem należy pobrać niezbędne biblioteki za pomocą komendy:
```console
pip install -r requirements.txt
```
Aby uruchomić aplikacje należy przy pomocy terminala wejść w folder z pobraną aplikacja i uruchomić ją za pomocą komendy:
```console
python main.py
```
Do sprawdzenia funkcjonalności aplikacji bedzie potrzebna nam także jej druga instancja. Otwieramy ja w takim sam sposób 
w drugim oknie terminala. 
<br />
<br />
Po uruchomieniu obu instancji jesteśmy gotowi do przejścia dalej. Jedną z aplikacji ustawiamy w tryb oczekiwania naciskjąc
przycisk ***Await Connection***. Nastepnie w drugiego oknie wpisujemy odpowiednie IP i naciskamy ***Connect***. Jeśli 
wszystko przebiegło bez problemu **Status** powinien zmienić sie na **Connected**. W tym momencie jesteśmy gotowi na 
rozpoczecie rozmowy.



