USERS = (
    ('Jan', 'Kowalski', 'jan@moj.pl', 'Mojehaslo1', 'Mojehaslo1'),
    ('Ewa', 'Niwińska', 'ewa@poczta.pl', 'Mojehaslo1', 'Mojehaslo1'),
    ('Tadeusz', 'Malinowski', 'tedeusz_1@moj.pl', 'Mojehaslo1', 'Mojehaslo1'),
    ('Sylwia', 'Adamska', 'sylwia@moj.pl', 'Mojehaslo1', 'Mojehaslo1'),
)

CATEGORIES = (
    "zabawki",
    "ubrania",
    "przybory szkolne",
    "narzędzia",
    "meble",
    "jedzenie",
    "sprzęt AGD",
)

INSTITUTIONS = (
    ('Zbiórka lokalna "My dzieciom"',
     'Cel i misja: Pomoc dzieciom z ubogich rodzin',
     ('zabawki', 'ubrania', 'przybory szkolne'),
     'LOCAL'),
    ('Zbieramy dla Kowalskich"',
     'Cel i misja: Pomoc rodzinie Kowalskich',
    ('narzędzia', 'ubrania', 'przybory szkolne', 'meble'),
     'LOCAL'),
    ('Organizacja “Dla dzieci"',
     'Cel i misja: Pomoc dzieciom',
     ('zabawki', 'ubrania', 'przybory szkolne', 'jedzenie'),
     'ORG'),
    ('Organizacja "Pomagamy starszym ludziom"',
     'Cel i misja: Pomoc osobom starszym i samotnym',
     ('jedzenie', 'ubrania', 'sprzęt AGD'),
     'ORG'),
    ("Fundacja “Bez domu”",
     'Cel i misja: Pomoc dla osób nie posiadających miejsca zamieszkania',
     ('narzędzia', 'ubrania', 'jedzenie'),
     ),
    ("Fundacja “Skrzywdzeni”",
     "Cel i misja: Pomagamy osobom, których doświadczył los",
     ('ubrania', 'jedzenie', 'sprzęt AGD', 'meble'),
     ),
    ('Zbiórka lokalna "My dzieciom_2"',
     'Cel i misja: Pomoc dzieciom z ubogich rodzin_2',
    ('zabawki', 'ubrania', 'przybory szkolne'),
     'LOCAL'),
    ('Zbieramy dla Kowalskich_2"',
     'Cel i misja: Pomoc rodzinie Kowalskich_2',
    ('zabawki', 'ubrania', 'jedzenie', 'sprzęt AGD'),
     'LOCAL'),
    ('Organizacja “Dla dzieci_2"',
     'Cel i misja: Pomoc dzieciom_2',
    ('zabawki', 'ubrania', 'jedzenie'),
     'ORG'),
    ('Organizacja "Pomagamy starszym ludziom"_2',
     'Cel i misja: Pomoc osobom starszym i samotnym_2',
    ('ubrania', 'jedzenie', 'sprzęt AGD'),
     'ORG'),
    ('Fundacja “Bez domu_2”',
     'Cel i misja: Pomoc dla osób nie posiadających miejsca zamieszkania_2',
    ('ubrania', 'jedzenie'),
     'FOUND'),
    ('Fundacja “Skrzywdzeni”_2',
     "Cel i misja: Pomagamy osobom, których doświadczył los_2",
    ('ubrania', 'jedzenie', 'sprzęt AGD', 'meble'),
     ),
    ('Zbiórka lokalna "My dzieciom_3"',
     'Cel i misja: Pomoc dzieciom z ubogich rodzin',
     ('zabawki', 'ubrania'),
     'LOCAL'),
    ('Organizacja "Pomagamy starszym ludziom"_3',
     'Cel i misja: Pomoc osobom starszym i samotnym_3',
     ('jedzenie', 'sprzęt AGD'),
     'ORG'),
    ('Organizacja "Pomagamy starszym ludziom"_4',
     'Cel i misja: Pomoc osobom starszym i samotnym_4',
     ('ubrania', 'jedzenie', 'sprzęt AGD', 'meble'),
     'ORG'),
)


DONATIONS = (
    (7,
    'Zbiórka lokalna "My dzieciom"',
    'Główna 1',
    "123-456-789",
    "Warszawa",
    "00-000",
    "2021-01-21",
    "14:00",
    "Proszę być punktualnie",
    ('zabawki', 'ubrania'),
    'jan@moj.pl',
     ),
    (2,
    'Zbieramy dla Kowalskich"',
    'Boczna 1',
    "555-444-222",
    "Wałbrzych",
    "11-999",
    "2021-05-12",
    "11:45",
    "Czekam cierpliwie",
    ('przybory szkolne', 'meble'),
    'ewa@poczta.pl',
     ),
    (10,
     'Organizacja “Dla dzieci"',
     'Niska 11',
     "321-444-888",
     "Zamość",
     "22-333",
     "2021-03-23",
     "16:45",
     "Brak uwag",
     ('zabawki', 'ubrania', 'jedzenie'),
     'jan@moj.pl',
     ),
    (3,
     'Organizacja "Pomagamy starszym ludziom"',
     'Zaułek Górski 112',
     "222-111-543",
     "Szczecin",
     "44-333",
     "2021-04-30",
     "20:45",
     "Ciężkie worki",
     ('jedzenie', 'ubrania'),
     'tedeusz_1@moj.pl',
     ),
    (12,
     'Zbiórka lokalna "My dzieciom_2"',
     'Śliska 1',
     "133-336-789",
     "Lublin",
     "11-222",
     "2021-10-01",
     "09:00",
     "Proszę być punktualnie",
     ('zabawki', 'ubrania'),
     'ewa@poczta.pl',
     ),
    (6,
     'Zbieramy dla Kowalskich_2"',
     'Kowalskiego 1',
     "555-222-222",
     "Wasilków",
     "11-222",
     "2021-09-11",
     "12:50",
     "Czekam cierpliwie",
     ('przybory szkolne', 'meble'),
     'ewa@poczta.pl',
     ),
    (1,
     'Organizacja “Dla dzieci"',
     'Pozioma 11',
     "321-111-888",
     "Grudziądz",
     "02-333",
     "2021-04-01",
     "10:45",
     "Brak uwag",
     ('zabawki', 'ubrania', 'jedzenie'),
     'tedeusz_1@moj.pl',
     ),
    (11,
     'Organizacja "Pomagamy starszym ludziom"',
     'Podworna 2',
     "222-111-333",
     "Ciechocinek",
     "44-222",
     "2021-07-22",
     "08:45",
     "Ciężkie worki",
     ('jedzenie', 'ubrania'),
     'sylwia@moj.pl',
     ),
)