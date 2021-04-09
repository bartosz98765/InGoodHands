import pytest
from ingoodhands.tests.utils import (bags_sum, institutions_sum, institution_sum_by_type, get_institution,
                                     get_category, get_donation, get_user_donations)
from ingoodhands.tests.data import DONATIONS, INSTITUTIONS, USERS
from django.contrib import auth
from django.contrib.auth.models import User


# ---------TESTS---------
@pytest.mark.django_db
def test_get_landingpage(client, add_users, setup):
    response = client.get('')
    assert response.status_code == 200
    assert response.context['bags_quantity'] == bags_sum(DONATIONS)
    assert response.context['institutions_quantity'] == institutions_sum(DONATIONS)
    assert len(response.context['foundations']) == institution_sum_by_type(INSTITUTIONS, 'FOUND')
    assert len(response.context['organizations']) == institution_sum_by_type(INSTITUTIONS, 'ORG')
    assert len(response.context['locals']) == institution_sum_by_type(INSTITUTIONS, 'LOCAL')


@pytest.mark.django_db
def test_anonymouse_user(client, add_users, setup):
    assert client.get('').status_code == 200

    response = client.get('/admin/')
    assert response.status_code == 302
    assert response['location'] == '/admin/login/?next=/admin/'

    response = client.get('/adddonation/')
    assert response.status_code == 302
    assert response['location'] == '/login/?next=/adddonation/'

    response = client.get('/confirmation/')
    assert response.status_code == 302
    assert response['location'] == '/login/?next=/confirmation/'

    response = client.get('/profile/')
    assert response.status_code == 302
    assert response['location'] == '/login/?next=/profile/'

    response = client.get('/userupdate/')
    assert response.status_code == 302
    assert response['location'] == '/login/?next=/userupdate/'

    response = client.get('/passwordchange/')
    assert response.status_code == 302
    assert response['location'] == '/login/?next=/passwordchange/'

    response = client.get('/get_inst_by_cat/')
    assert response.status_code == 302
    assert response['location'] == '/login/'


@pytest.mark.django_db
def test_register_login_update_pswchange_view(client):
    # user register test
    ctx = {'username': USERS[0][2],
           'first_name': USERS[0][0],
           'last_name': USERS[0][1],
           'password1': USERS[0][3],
           'password2': USERS[0][4],
           }
    response = client.post('/register/', ctx)
    assert response.status_code == 302
    assert response['location'] == '/login/'

    # user login test
    ctx = {'username': USERS[0][2], 'password': USERS[0][3]}
    response = client.post('/login/', ctx)
    assert response.status_code == 302
    assert response['location'] == '/'
    user = auth.get_user(response.wsgi_request)
    assert user == User.objects.get(username=USERS[0][2])

    # user data change test
    ctx = {'user_update-username': 'marta@moj.pl',
           'user_update-first_name': 'Marta',
           'user_update-last_name': 'Kowalska',
           'user_update-confirm_password': 'Mojehaslo1',
           }
    response = client.post('/userupdate/', ctx)
    assert response.status_code == 302
    user = auth.get_user(response.wsgi_request)
    assert user.username == ctx['user_update-username'] \
           and user.first_name == ctx['user_update-first_name'] \
           and user.last_name == ctx['user_update-last_name']

    # user password change test
    ctx = {'password_change-actual_password': 'Mojehaslo1',
           'password_change-password': 'Mojehaslo222',
           'password_change-password2': 'Mojehaslo222',
           }
    response = client.post('/passwordchange/', ctx)
    assert response.status_code == 302
    response = client.get('/passwordchange/')
    user = auth.get_user(response.wsgi_request)
    assert user == User.objects.get(username='marta@moj.pl')

    # adddonation form test


@pytest.mark.django_db
def test_form(client, add_users, setup):
    client.login(username=USERS[0][2], password=USERS[0][3])
    keys = ('quantity', 'institution', 'address', 'phone_number', 'city',
            'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment', 'categories')
    values = DONATIONS[0][:-1]
    ctx = dict(zip(keys, values))
    ctx['institution'] = get_institution(ctx['institution']).pk
    ctx['categories'] = [get_category(cat).pk for cat in ctx['categories']]
    response = client.post('/adddonation/', ctx)
    assert response.status_code == 302
    assert get_donation().quantity == ctx['quantity']
    assert len(get_donation().categories.all()) == len(ctx['categories'])
    user = auth.get_user(response.wsgi_request)
    assert get_donation().user == user


@pytest.mark.django_db
def test_profile(client, add_users, setup):
    client.login(username=USERS[3][2], password=USERS[3][3])
    # user data test
    response = client.get('/profile/')
    assert response.status_code == 200
    user = auth.get_user(response.wsgi_request)
    assert f'{user.first_name} {user.last_name} {user.username}' in response.content.decode()
    # user donation list test
    donations = get_user_donations(user.username)
    assert len(donations) == 1
    for donation in donations:
        assert donation.is_taken == False
    # change user donation status test
    ctx = {'is_taken': donations.first().pk}
    response = client.post('/profile/', ctx)
    donations = get_user_donations(user.username)
    assert donations.last().is_taken == True
