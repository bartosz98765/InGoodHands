# from random import sample, randint, choice
# from faker import Faker
from ingoodhands.models import Category, Institution, Donation
from django.contrib.auth.models import User, Permission


# faker = Faker("pl_PL")


def create_categories(categories):
    for category in categories:
        Category.objects.create(name=category)


def get_category(name):
    return Category.objects.get(name=name)


def create_institutions(institutions):
    for inst in institutions:
        if len(inst) == 4:
            institution = Institution.objects.create(name=inst[0], description=inst[1], type=inst[3])
        else:
            institution = Institution.objects.create(name=inst[0], description=inst[1])
        for category in inst[2]:
            institution.categories.add(get_category(category))


def get_institution(name):
    return Institution.objects.get(name=name)


def create_users(users):
    for user in users:
        new_user = User.objects.create_user(
            username=user[2],
            first_name=user[0],
            last_name=user[1],
            password=user[3],
        )
        new_user.user_permissions.add(Permission.objects.get(codename='add_donation'))


def get_user(username):
    return User.objects.get(username=username)


def get_first_user():
    return User.objects.all().first()


def create_donations(donations):
    for donation in donations:
        donat = Donation.objects.create(
            quantity=donation[0],
            institution=get_institution(donation[1]),
            address=donation[2],
            phone_number=donation[3],
            city=donation[4],
            zip_code=donation[5],
            pick_up_date=donation[6],
            pick_up_time=donation[7],
            pick_up_comment=donation[8],
            user=get_user(donation[10]),
        )
        for category in donation[9]:
            donat.categories.add(get_category(category))


def get_donation():
    return Donation.objects.all().first()

def get_user_donations(username):
    return Donation.objects.filter(user__username=username)

def bags_sum(donations):
    return sum(el[0] for el in donations)


def institutions_sum(donations):
    return len(set(el[1] for el in donations))


def institution_sum_by_type(institutions, type):
    i = 0
    for el in institutions:
        if len(el) == 4:
            if el[3] == type:
                i += 1
        if type == 'FOUND':
            if len(el) == 3:
                i += 1
    return i
