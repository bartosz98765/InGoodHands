import pytest
from ingoodhands.tests.utils import bags_sum, institutions_sum, institution_sum_by_type, get_first_user
from ingoodhands.tests.data import DONATIONS, INSTITUTIONS


# ---------TESTS---------
@pytest.mark.django_db
def test_get_landingpage(client, setup):
    response = client.get('')
    assert response.status_code == 200
    assert response.context['bags_quantity'] == bags_sum(DONATIONS)
    assert response.context['institutions_quantity'] == institutions_sum(DONATIONS)
    assert len(response.context['foundations']) == institution_sum_by_type(INSTITUTIONS, 'FOUND')
    assert len(response.context['organizations']) == institution_sum_by_type(INSTITUTIONS, 'ORG')
    assert len(response.context['locals']) == institution_sum_by_type(INSTITUTIONS, 'LOCAL')


@pytest.mark.django_db
def test_anonymouse_user(client, setup):
    assert client.get('').status_code == 200

    response = client.get('/admin/')
    assert response.status_code == 302
    assert response['location'] == '/admin/login/?next=/admin/'

    response = client.get('/adddonation/')
    assert response.status_code == 302
    assert response['location'] == '/login/?next=/adddonation/'

    response = client.get(f'/profile/{get_first_user().pk}')
    assert response.status_code == 301