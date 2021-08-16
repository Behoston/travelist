# Travelist

Zadanie rekrutacyjne do [Travelist](https://travelist.pl).

Postanowiłem, że aplikacja będzie kasynem, bo to pierwsze co pomyślałem, widząc żetony.

## Treść zadania

<details>

Celem zadania jest zaprojektowanie i zaimplementowanie systemu płatności wirtualną walutą (punktami) w ramach aplikacji
Django. Punkty mogą pochodzić z różnych źródeł np. bonusów za rezerwacje, wygranych w konkursie, kuponów promocyjnych,
polecenia innym użytkownikom systemu oraz innych nieprzewidzianych w systemie - potencjalnie mogą dochodzić nowe źródła
punktów.

Zadanie składa się z dwóch części: webserwisu i importera danych. Webserwis do zarządzania stanem konta użytkowników

Należy zaprojektować i zakodować apkę Django 2, która zrealizuje następujące operacje:

1. Listowanie wszystkich użytkowników wraz z ich aktualnym stanem konta.
2. Podstrona, na której dowolnemu użytkownikowi można przyznać lub odebrać środki (w dowolnej wysokości, z dowolnego
   tytułu)

Importer dla załączonego pliku CSV

Do zadania dołączony jest plik: users.csv, w którym zawarte są następujące dane użytkowników:

    id
    first_name
    last_name
    email
    balance - stan konta, liczba punktów do wykorzystania
    referrer_email - email użytkownika polecającego

Należy napisać importer danych do systemu z pliku users.csv. Powinna być możliwość uruchomienia importera z poziomu
wiersza poleceń w następujący sposób `./manage.py import_users_data users.csv`. Jeśli importowany użytkownik został
przez kogoś polecony (tzn. ma wpisany email użytkownika polecającego) należy osobie polecającej z tego tytułu dopisać 20
punktów do stanu konta.

Przydatne informacje:

1. Rozwiązaniem zadania powinien być link do repozytorium git, w którym jest kod rozwiązania, oraz instrukcja jak je
   uruchomić.
2. Można użyć dowolnych bibliotek, które mogą się przydać przy implementacji rozwiązania.
3. Strona wizualna nie podlega ocenie.
4. Tak jak zaznaczyłem, nie musisz zrobić wszystkiego, co jest wg Ciebie tam potrzebne, ale jeśli czegoś nie zrobisz, to
   wrzuć do readme, co by się jeszcze przydało, czy na co trzeba zwrócić uwagę

</details>

## Requirements

- docker
- docker-compose version 3

## How to run

```bash
docker-compose up
```

## How to import data

```bash
docker ps
# Find your backend container and copy ID
docker cp ./resources/sample_data.csv 17a6ea101925:/tmp/sample.csv
docker-compose exec backend bash
python manage.py import_users_data /tmp/sample.csv
```

## Issues

- Not prod build (debug=true, runserver instead of gunicorn, missing reverse proxy, all hosts allowed)
- Not explicite required to log why user granted points, so due to `YAGNI` I do not implemented separate table for
  points.
- No tests.
- No reversed urls.
