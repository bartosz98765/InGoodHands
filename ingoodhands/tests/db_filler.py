from ingoodhands.models import *

donations = Donation.objects.all()
donations.delete()

institutions = Institution.objects.all()
institutions.delete()

categories = Category.objects.all()
categories.delete()


# CATEGORIES

category_1 = Category.objects.create(name="zabawki")
category_2 = Category.objects.create(name="ubrania")
category_3 = Category.objects.create(name="przybory szkolne")
category_4 = Category.objects.create(name="narzędzia")
category_5 = Category.objects.create(name="meble")
category_6 = Category.objects.create(name="jedzenie")
category_7 = Category.objects.create(name="sprzęt AGD")

# INSTITUTIONS

inst_1 = Institution.objects.create(
    name='Zbiórka lokalna "My dzieciom"',
    description="Cel i misja: Pomoc dzieciom z ubogich rodzin.",
    type='LOCAL'
)
inst_1.categories.add(category_1, category_2, category_3, category_5, category_6)

inst_4 = Institution.objects.create(
    name='Zbieramy dla Kowalskich"',
    description="Cel i misja: Pomoc rodzinie Kowalskich.",
    type='LOCAL'
)
inst_4.categories.add(category_1, category_2, category_3, category_4, category_5, category_6)

inst_2 = Institution.objects.create(
    name='Organizacja “Dla dzieci"',
    description="Cel i misja: Pomoc dzieciom.",
    type='ORG'
)
inst_2.categories.add(category_1, category_2, category_3, category_4, category_7)

inst_5 = Institution.objects.create(
    name='Organizacja "Pomagamy starszym ludziom"',
    description="Cel i misja: Pomoc osobom starszym i samotnym.",
    type='ORG'
)
inst_5.categories.add(category_1, category_2, category_4, category_6, category_7)

inst_3 = Institution.objects.create(
    name="Fundacja “Bez domu”",
    description="Cel i misja: Pomoc dla osób nie posiadających miejsca zamieszkania",
)
inst_3.categories.add(category_2, category_6)

inst_6 = Institution.objects.create(
    name="Fundacja “Skrzywdzeni”",
    description="Cel i misja: Pomagamy osobom, których doświadczył los",
)
inst_6.categories.add(category_1, category_2, category_3, category_4, category_5, category_6, category_7)


inst_7 = Institution.objects.create(
    name='Zbiórka lokalna "My dzieciom 2"',
    description="Cel i misja: Pomoc dzieciom z ubogich rodzin.",
    type='LOCAL'
)
inst_7.categories.add(category_1, category_2, category_3, category_5, category_6)

inst_8 = Institution.objects.create(
    name='Zbieramy dla Kowalskich 2"',
    description="Cel i misja: Pomoc rodzinie Kowalskich.",
    type='LOCAL'
)
inst_8.categories.add(category_1, category_2, category_3, category_4, category_5, category_6)

inst_9 = Institution.objects.create(
    name='Organizacja “Dla dzieci 2"',
    description="Cel i misja: Pomoc dzieciom.",
    type='ORG'
)
inst_9.categories.add(category_1, category_2, category_3, category_4, category_7)

inst_10 = Institution.objects.create(
    name='Organizacja "Pomagamy starszym ludziom 2"',
    description="Cel i misja: Pomoc osobom starszym i samotnym.",
    type='ORG'
)
inst_10.categories.add(category_1, category_2, category_4, category_6, category_7)

inst_11 = Institution.objects.create(
    name="Fundacja “Bez domu 2”",
    description="Cel i misja: Pomoc dla osób nie posiadających miejsca zamieszkania",
)
inst_11.categories.add(category_2, category_6)

inst_12 = Institution.objects.create(
    name="Fundacja “Skrzywdzeni 2”",
    description="Cel i misja: Pomagamy osobom, których doświadczył los",
)
inst_12.categories.add(category_1, category_2, category_3, category_4, category_5, category_6, category_7)

inst_13 = Institution.objects.create(
    name="Fundacja “Bez domu 3”",
    description="Cel i misja: Pomoc dla osób nie posiadających miejsca zamieszkania",
)
inst_13.categories.add(category_2, category_6)

inst_14 = Institution.objects.create(
    name="Fundacja “Skrzywdzeni 3”",
    description="Cel i misja: Pomagamy osobom, których doświadczył los",
)
inst_14.categories.add(category_1, category_2, category_3, category_4, category_5, category_6, category_7)









# DONATIONS

donation_1 = Donation.objects.create(
    quantity=7,
    institution=inst_1,
    address="Główna 1",
    phone_number="123-456-789",
    city="Warszawa",
    zip_code="00-000",
    pick_up_date="2021-01-21",
    pick_up_time="14:00",
    pick_up_comment="Proszę być punktualnie",
)
donation_1.categories.add(category_1, category_2)

donation_2 = Donation.objects.create(
    quantity=2,
    institution=inst_1,
    address="Główna 2",
    phone_number="123-456-789",
    city="Warszawa",
    zip_code="00-000",
    pick_up_date="2021-02-05",
    pick_up_time="4:00",
    pick_up_comment="Proszę być punktualnie",
)
donation_2.categories.add(category_2, category_3)

donation_3 = Donation.objects.create(
    quantity=2,
    institution=inst_1,
    address="Główna 2",
    phone_number="123-456-789",
    city="Warszawa",
    zip_code="00-000",
    pick_up_date="2021-02-05",
    pick_up_time="10:10",
    pick_up_comment="Proszę być punktualnie",
)
donation_3.categories.add(category_2)

donation_4 = Donation.objects.create(
    quantity=1,
    institution=inst_1,
    address="Główna 1",
    phone_number="123-456-789",
    city="Warszawa",
    zip_code="00-000",
    pick_up_date="2021-01-05",
    pick_up_time="18:50",
    pick_up_comment="Proszę być punktualnie",
)
donation_4.categories.add(category_1, category_2)

donation_5 = Donation.objects.create(
    quantity=1,
    institution=inst_3,
    address="Główna 1",
    phone_number="123-456-789",
    city="Warszawa",
    zip_code="00-000",
    pick_up_date="2021-03-05",
    pick_up_time="12:00",
    pick_up_comment="Proszę być punktualnie",
)
donation_5.categories.add(category_5)
